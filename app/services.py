# app/services.py

import logging
from datetime import datetime
import requests
import google.generativeai as genai

# Import config and prompts from our app package
from app.config import config
from app.prompts import SYSTEM_PROMPT

# In-memory store (will reset on serverless function cold starts)
CONVERSATION_STORE = {}

# --- AI & DATA TOOLS ---
def get_historical_data_for_graphing(tickers: list, date_range: str = "past year"):
    """Fetches historical price data for one or more stock tickers for the purpose of creating a graph."""
    return FinancialDataService.get_historical_data(tickers, date_range)

def get_real_time_quote(ticker: str):
    """Gets the real-time stock quote for a single ticker, automatically detecting if it's a stock or cryptocurrency."""
    return FinancialDataService.get_real_time_quote(ticker)

# --- SERVICE CLASSES ---
class FinancialDataService:
    """Handles all interactions with the RapidAPI Yahoo Finance service."""
    API_HOST = "yahoo-finance15.p.rapidapi.com"
    
    @staticmethod
    def _get_headers():
        return {"x-rapidapi-key": config.RAPIDAPI_KEY.strip(), "x-rapidapi-host": FinancialDataService.API_HOST}

    @staticmethod
    def _map_date_range_to_params(date_range_str):
        date_range_str = date_range_str.lower()
        if "year" in date_range_str: return {"interval": "1d", "limit": 252}
        if "6 month" in date_range_str: return {"interval": "1d", "limit": 126}
        if "month" in date_range_str: return {"interval": "1d", "limit": 22}
        if "week" in date_range_str: return {"interval": "1d", "limit": 7}
        return {"interval": "1d", "limit": 252}

    @staticmethod
    def get_historical_data(tickers, date_range_str="past year"):
        params = FinancialDataService._map_date_range_to_params(date_range_str)
        processed_data = {}
        for ticker in tickers:
            ticker = ticker.upper()
            url = f"https://{FinancialDataService.API_HOST}/api/v2/markets/stock/history"
            querystring = {"symbol": ticker, "interval": params["interval"], "limit": params["limit"]}
            try:
                response = requests.get(url, headers=FinancialDataService._get_headers(), params=querystring)
                response.raise_for_status()
                data = response.json()
                if not data.get('body'):
                    processed_data[ticker] = []
                    continue
                sorted_data = sorted(data['body'], key=lambda x: x.get('timestamp', 0))
                temp_data = []
                for item in sorted_data:
                    if 'timestamp' in item and 'close' in item:
                        try:
                            date_str = datetime.fromtimestamp(int(item['timestamp'])).strftime('%Y-%m-%d')
                        except (ValueError, TypeError):
                            date_str = str(item['timestamp'])
                        temp_data.append({"year": date_str, "price": round(item['close'], 2)})
                processed_data[ticker] = temp_data
            except Exception as e:
                logging.error(f"RapidAPI historical data request failed for {ticker}: {e}")
                processed_data[ticker] = []
        return processed_data

    @staticmethod
    def get_real_time_quote(ticker):
        ticker = ticker.upper()
        url = f"https://{FinancialDataService.API_HOST}/api/v1/markets/quote"
        asset_type = "CRYPTO" if "-" in ticker else "STOCKS"
        querystring = {"ticker": ticker, "type": asset_type}
        try:
            response = requests.get(url, headers=FinancialDataService._get_headers(), params=querystring)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, dict) and data.get('body'):
                return data['body']
            return {"error": "No 'body' key found in the quote response."}
        except Exception as e:
            logging.error(f"RapidAPI real-time quote request failed for {ticker}: {e}")
            return {"error": f"API request failed: {e}"}

class GoogleAIService:
    """Handles all interactions with the Google Generative AI API."""
    def __init__(self):
        self.model = genai.GenerativeModel(model_name=config.MODEL_NAME, system_instruction=SYSTEM_PROMPT, tools=[get_historical_data_for_graphing, get_real_time_quote])

    def generate_response(self, history, user_message):
        gemini_history = [{"role": "model" if msg["role"] == "assistant" else "user", "parts": [{"text": msg["text"]}]} for msg in history]
        chat = self.model.start_chat(history=gemini_history)
        try:
            return chat.send_message(user_message)
        except Exception as e:
            logging.error(f"Google AI API Error: {e}")
            raise RuntimeError(f"AI model communication failed: {e}")

    def generate_title(self, message):
        try:
            model = genai.GenerativeModel(config.MODEL_NAME)
            prompt = f"Generate a concise (4-5 word) title for a financial analysis conversation starting with: '{message}'"
            response = model.generate_content(prompt)
            return response.text.strip().replace('"', '')
        except Exception as e:
            logging.error(f"Title generation failed: {e}")
            return "New Conversation"
