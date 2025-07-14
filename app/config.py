# app/config.py

import os
import google.generativeai as genai

class AppConfig:
    """A class to hold all application configuration and secrets."""
    def __init__(self):
        # On Vercel, secrets are loaded from environment variables.
        self.GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
        self.RAPIDAPI_KEY = os.environ.get('RAPIDAPI_KEY')
        self.MODEL_NAME = "gemini-2.5-pro"
        
        if not self.GOOGLE_API_KEY or not self.RAPIDAPI_KEY:
            raise ValueError("API keys (GOOGLE_API_KEY, RAPIDAPI_KEY) are not set as environment variables.")
        
        genai.configure(api_key=self.GOOGLE_API_KEY)

# Create a single configuration instance to be used throughout the app
config = AppConfig()
