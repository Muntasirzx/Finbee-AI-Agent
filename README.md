<p align="center">
  <img src="https://i.imgur.com/your-image-url-for-finbee-logo.png" alt="Finbee AI Logo" width="120"/>
</p>

<h1 align="center">Finbee AI</h1>

<p align="center">
  An AI-powered financial analyst with the persona of a Wall Street broker, designed to provide decisive, real-time investment insights for both stocks and cryptocurrencies.
</p>

<p align="center">
  <img alt="Status" src="https://img.shields.io/badge/status-live-success.svg">
  <img alt="Vercel" src="https://img.shields.io/badge/deployed%20on-Vercel-black?logo=vercel">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.9-blue.svg?logo=python">
  <img alt="Flask" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
  <img alt="Gemini" src="https://img.shields.io/badge/Powered%20by-Gemini%202.5%20Pro-purple.svg">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Muntasirzx/Finbee-AI-Agent/61485d4879278031d8a3c84fbd1453c9cbf746a0/DATA/_init_.gif" alt="Finbee AI Interface" width="49%"/>
  <img src="https://raw.githubusercontent.com/Muntasirzx/Finbee-AI-Agent/61485d4879278031d8a3c84fbd1453c9cbf746a0/DATA/2.png" alt="Finbee AI Interface" width="49%"/>
</p>

---

## ✨ Features

* **Decisive AI Persona:** Get direct "Buy," "Sell," or "Hold" recommendations, backed by data—no hedging or disclaimers.
* **Real-Time Data:** Integrated with the Yahoo Finance API for up-to-the-minute stock and crypto quotes.
* **Dynamic Charting:** On-demand historical performance charts rendered directly in the chat.
* **Conversational Profiling:** Engages with users to understand their risk tolerance and investment goals before providing tailored crypto recommendations.
* **Multi-Asset Support:** Seamlessly provides analysis for both equities and cryptocurrencies.

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine for development and testing purposes.

### Prerequisites

* Python 3.9+
* Git
* A [RapidAPI](https://rapidapi.com/hub) account and a Yahoo Finance API subscription key.
* A [Google AI Studio](https://aistudio.google.com/) API key for Gemini.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/finbee-ai-app.git](https://github.com/your-username/finbee-ai-app.git)
    cd finbee-ai-app
    ```

2.  **Create and activate a virtual environment:**
    * **Mac/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * **Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    * Create a new file named `.env` in the root of the project.
    * Add your secret keys to this file. This file is listed in `.gitignore` and will not be committed to your repository.
        ```
        # .env file
        GOOGLE_API_KEY="your-actual-google-api-key"
        RAPIDAPI_KEY="your-actual-rapidapi-key"
        ```

5.  **Run the application:**
    * The project uses a local development server. To run it, you'll need a library like `python-dotenv` to load your `.env` file. First, install it:
        ```bash
        pip install python-dotenv
        ```
    * Then, create a new file named `run_local.py` in the root directory. This will be our local entry point.
        ```python
        # run_local.py
        from dotenv import load_dotenv
        load_dotenv() # Load environment variables from .env file

        from app import app

        if __name__ == "__main__":
            app.run(debug=True, port=5001)
        ```
    * Now, start the local server:
        ```bash
        python run_local.py
        ```
    * Open your browser and navigate to `http://127.0.0.1:5001` to use the application.

---

## 🛠️ Technology Stack

| Frontend                                                                                                                                              | Backend                                                                                                                                 | AI & Data                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">                         | <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">                      | <img src="https://img.shields.io/badge/Gemini_API-8E75B2?style=for-the-badge&logo=google-gemini&logoColor=white" alt="Gemini API">         |
| <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS">                   | <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">                          | <img src="https://img.shields.io/badge/RapidAPI-3B3B58?style=for-the-badge&logo=rapidapi&logoColor=white" alt="RapidAPI">                |
| <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">                                         | <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel">                        |                                                                                                                                                     |

---

## 🌐 Deployment

This application is configured for seamless deployment on **Vercel**.

1.  Push the code to a GitHub repository.
2.  Import the repository into Vercel.
3.  Add the `GOOGLE_API_KEY` and `RAPIDAPI_KEY` as Environment Variables in the Vercel project settings.
4.  Vercel will automatically detect the `vercel.json` file and deploy the application as a Python Serverless Function.

Any subsequent `git push` to the `main` branch will trigger an automatic redeployment with the latest changes.

---

## 🏛️ How It Works: The Agentic Workflow

<p align="center">
  <!-- Replace with your actual image URL -->
  <img src="https://i.imgur.com/2.png" alt="Finbee AI Architecture" width="800"/>
</p>

Finbee operates on a sophisticated agentic loop powered by Gemini's function-calling capabilities.

1.  **Orchestration:** The Flask backend serves as the main orchestrator. It receives user requests and manages the state of the conversation.
2.  **Reasoning & Tool Selection:** The user's prompt, along with the conversation history, is sent to the Gemini 2.5 Pro model. The model, guided by its detailed **System Prompt**, analyzes the request and decides if it can answer directly or if it needs to use a tool to gather live data.
3.  **Function Calling:** If the model decides to use a tool (e.g., `get_real_time_quote`), it returns the function name and the necessary arguments (e.g., `ticker='AAPL'`).
4.  **Data Retrieval:** The Flask backend executes the corresponding Python function, which makes a secure API call to the RapidAPI service.
5.  **Response Generation:** The fetched data is sent back to the Gemini model. Now equipped with real-time information, the model generates its final, data-driven, and decisive response in the persona of a Wall Street analyst.
