# app/routes.py

import time
import json
import logging
from flask import request, jsonify, render_template_string

# Import the app object and service classes
from app import app
from app.services import GoogleAIService, FinancialDataService, CONVERSATION_STORE
from app.templates import HOME_PAGE_TEMPLATE, CHAT_PAGE_TEMPLATE

@app.route('/', methods=['GET'])
def home():
    """Serves the home page."""
    return render_template_string(HOME_PAGE_TEMPLATE)

@app.route('/chat', methods=['GET'])
def chat_page():
    """Serves the chat page."""
    return render_template_string(CHAT_PAGE_TEMPLATE)

@app.route('/api/conversations', methods=['POST'])
def create_conversation():
    """Creates a new, empty conversation."""
    session_id = request.json.get('sessionId')
    if not session_id: return jsonify({"error": "Session ID is required"}), 400
    if session_id not in CONVERSATION_STORE: CONVERSATION_STORE[session_id] = {}
    convo_id = f"convo_{int(time.time())}"
    new_convo = {"id": convo_id, "title": "New Conversation", "messages": [], "timestamp": time.time()}
    CONVERSATION_STORE[session_id][convo_id] = new_convo
    return jsonify(new_convo), 201

@app.route('/api/conversations/<convo_id>/messages', methods=['POST'])
def send_message(convo_id):
    """Handles sending a message and getting the AI's response."""
    session_id = request.args.get('sessionId')
    user_message = request.json.get('message')
    if not session_id or not user_message or convo_id not in CONVERSATION_STORE.get(session_id, {}):
        return jsonify({"error": "Invalid request"}), 400
    
    conversation = CONVERSATION_STORE[session_id][convo_id]
    history = conversation["messages"]
    
    try:
        google_ai_service = GoogleAIService()
        response = google_ai_service.generate_response(history, user_message)
        final_response_text = ""
        response_part = response.candidates[0].content.parts[0]

        if hasattr(response_part, 'function_call') and response_part.function_call:
            function_call = response_part.function_call
            if function_call.name == 'get_historical_data_for_graphing':
                args = {k: v for k, v in function_call.args.items()}
                tickers = args.get("tickers", [])
                date_range = args.get("date_range", "past year")
                real_data = FinancialDataService.get_historical_data(tickers, date_range)
                graph_json = {"graph_data": {"type": "time_series", "title": f"Stock Prices for {', '.join(tickers)}", "series": [{"name": ticker, "data": real_data.get(ticker, [])} for ticker in tickers]}}
                final_response_text = f"Here is the chart you requested for {', '.join(tickers)}.\n```json\n{json.dumps(graph_json, indent=2)}\n```"
            elif function_call.name == 'get_real_time_quote':
                args = {k: v for k, v in function_call.args.items()}
                ticker = args.get("ticker")
                quote_data = FinancialDataService.get_real_time_quote(ticker)
                if "error" not in quote_data:
                    primary_data = quote_data.get('primaryData', {})
                    price = primary_data.get('lastSalePrice', 'N/A')
                    change = primary_data.get('netChange', 'N/A')
                    change_pct = primary_data.get('percentageChange', 'N/A')
                    name = quote_data.get('companyName', ticker)
                    final_response_text = f"**{name} ({ticker.upper()})** is currently trading at **{price}**. Today's change is {change} ({change_pct})."
                else:
                    final_response_text = f"Sorry, I couldn't retrieve the real-time quote for {ticker}. Reason: {quote_data['error']}"
            else:
                final_response_text = f"I encountered an unknown tool '{function_call.name}'. Please try again."
        elif hasattr(response_part, 'text') and response_part.text:
            final_response_text = response_part.text
        else:
            final_response_text = "Sorry, I received an unexpected response from the AI."

        history.append({"role": "user", "text": user_message})
        history.append({"role": "assistant", "text": final_response_text})
        response_data = {"message": {"role": "assistant", "text": final_response_text}}
        if len([m for m in history if m['role'] == 'user']) == 1:
            new_title = google_ai_service.generate_title(user_message)
            conversation["title"] = new_title
            response_data["title"] = new_title
        return jsonify(response_data), 200
    except Exception as e:
        logging.error(f"Message handling error: {e}")
        return jsonify({"error": str(e)}), 500
