
<div align="center">
  <img src="https://raw.githubusercontent.com/Muntasirzx/Finbee-AI-Agent/e5a3792bb59296f5149fe7e53e8cd1a48da17b75/DATA/STREIGHT%20out%20of.png" width="120"/>
  
  <h1>Finbee AI</h1>
  
  <p>
    <strong>Real-time market analysis • Decisive investment strategies • Wall Street-grade insights</strong>
  </p>
  
  <p>
    <img alt="Status" src="https://img.shields.io/badge/status-live-success.svg?style=for-the-badge&logo=checkmarx&logoColor=white">
    <img alt="Vercel" src="https://img.shields.io/badge/deployed%20on-Vercel-black?style=for-the-badge&logo=vercel&logoColor=white">
    <img alt="Python" src="https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white">
    <img alt="Flask" src="https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white">
    <img alt="Gemini" src="https://img.shields.io/badge/Powered%20by-Gemini%202.5%20Pro-purple.svg?style=for-the-badge&logo=google&logoColor=white">
  </p>
  
  <br>
  
  <div>
    <img src="https://raw.githubusercontent.com/Muntasirzx/Finbee-AI-Agent/61485d4879278031d8a3c84fbd1453c9cbf746a0/DATA/_init_.gif" alt="Finbee AI Interface" width="49%"/>
    <img src="https://raw.githubusercontent.com/Muntasirzx/Finbee-AI-Agent/61485d4879278031d8a3c84fbd1453c9cbf746a0/DATA/2.png" alt="Finbee AI Interface" width="49%"/>
  </div>
  
  <br>
  
  <a href="https://finbee-ai-agent.vercel.app/" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/_Launch_Finbee_AI-00000?style=for-the-badge&logo=rocket&logoColor=white&labelColor=808080" alt="Launch Finbee AI" height="50">
  </a>
</div>

---

## 🎯 Core Features

<table>
  <tr>
    <td width="50%">
      <h3>🧠 Intelligent Decision Engine</h3>
      <p>Get direct <strong>Buy</strong>, <strong>Sell</strong>, or <strong>Hold</strong> recommendations backed by real-time data analysis—no hedging, just decisive Wall Street-grade insights.</p>
    </td>
    <td width="50%">
      <h3>📊 Real-Time Market Data</h3>
      <p>Integrated with Yahoo Finance API for up-to-the-minute stock and cryptocurrency quotes with sub-second latency.</p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>📈 Dynamic Visualization</h3>
      <p>On-demand historical performance charts and technical indicators rendered directly in the chat interface.</p>
    </td>
    <td width="50%">
      <h3>🎪 Conversational Profiling</h3>
      <p>AI-driven risk assessment and investment goal analysis for personalized portfolio recommendations.</p>
    </td>
  </tr>
</table>

<div align="center">
  <img src="https://img.shields.io/badge/Multi_Asset_Support-Stocks_•_Crypto_•_Futures-brightgreen?style=for-the-badge&logo=trending-up&logoColor=white" alt="Multi-Asset Support">
</div>

---

## 🚀 Quick Start Guide

### 📋 Prerequisites

<table>
  <tr>
    <td><img src="https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python&logoColor=white"></td>
    <td><img src="https://img.shields.io/badge/Git-Latest-red?style=flat-square&logo=git&logoColor=white"></td>
    <td><img src="https://img.shields.io/badge/RapidAPI-Account-purple?style=flat-square&logo=rapidapi&logoColor=white"></td>
    <td><img src="https://img.shields.io/badge/Google_AI-Studio-orange?style=flat-square&logo=google&logoColor=white"></td>
  </tr>
</table>

### 💻 Installation

<details>
<summary><strong>🔧 Step-by-Step Setup</strong></summary>

#### 1. Clone Repository
```bash
git clone https://github.com/your-username/finbee-ai-app.git
cd finbee-ai-app
```

#### 2. Environment Setup
**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Configure Environment Variables
Create `.env` file:
```env
# API Configuration
GOOGLE_API_KEY="your-actual-google-api-key"
RAPIDAPI_KEY="your-actual-rapidapi-key"
```

#### 5. Local Development Server
Create `run_local.py`:
```python
# run_local.py
from dotenv import load_dotenv
load_dotenv()

from app import app

if __name__ == "__main__":
    app.run(debug=True, port=5001)
```

#### 6. Launch Application
```bash
python run_local.py
```

Navigate to `http://127.0.0.1:5001`

</details>

---

## 🏗️ Technology Architecture

<div align="center">
  
### Frontend Stack
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
<img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS">
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">

### Backend Infrastructure
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
<img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel">

### AI & Data Layer
<img src="https://img.shields.io/badge/Gemini_API-8E75B2?style=for-the-badge&logo=google-gemini&logoColor=white" alt="Gemini API">
<img src="https://img.shields.io/badge/RapidAPI-3B3B58?style=for-the-badge&logo=rapidapi&logoColor=white" alt="RapidAPI">
<img src="https://img.shields.io/badge/Yahoo_Finance-720E9E?style=for-the-badge&logo=yahoo&logoColor=white" alt="Yahoo Finance">

</div>

---

## 🌐 Production Deployment

<div align="center">
  <img src="https://img.shields.io/badge/One_Click_Deploy-Vercel-black?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel Deploy">
</div>

### Deployment Pipeline

1. **Repository Setup**: Push code to GitHub repository
2. **Vercel Integration**: Import repository into Vercel dashboard
3. **Environment Configuration**: Add `GOOGLE_API_KEY` and `RAPIDAPI_KEY` to Vercel environment variables
4. **Automatic Deployment**: Vercel detects `vercel.json` and deploys as Python Serverless Function

<div align="center">
  <img src="https://img.shields.io/badge/Auto_Deploy-main_branch-success?style=for-the-badge&logo=github-actions&logoColor=white" alt="Auto Deploy">
</div>

> **Note**: Any push to `main` branch triggers automatic redeployment with zero downtime.

---

## 🔄 Agentic Workflow Architecture

<div align="center">
  <img src="https://raw.githubusercontent.com/Muntasirzx/Finbee-AI-Agent/e68df93913412215d208a6d894105f674a141acb/DATA/3.png" width="100%" alt="Agentic Workflow"/>
</div>

### Intelligence Flow

<table>
  <tr>
    <td width="20%" align="center">
      <img src="https://img.shields.io/badge/1-Orchestration-blue?style=for-the-badge&logo=gear&logoColor=white" alt="Step 1">
    </td>
    <td width="80%">
      <strong>Request Processing</strong><br>
      Flask backend receives user requests and maintains conversation state with session management.
    </td>
  </tr>
  <tr>
    <td width="20%" align="center">
      <img src="https://img.shields.io/badge/2-AI_Reasoning-purple?style=for-the-badge&logo=brain&logoColor=white" alt="Step 2">
    </td>
    <td width="80%">
      <strong>Intelligent Analysis</strong><br>
      Gemini 2.5 Pro analyzes context and determines optimal response strategy using advanced reasoning.
    </td>
  </tr>
  <tr>
    <td width="20%" align="center">
      <img src="https://img.shields.io/badge/3-Function_Calling-orange?style=for-the-badge&logo=api&logoColor=white" alt="Step 3">
    </td>
    <td width="80%">
      <strong>Tool Selection</strong><br>
      AI selects appropriate tools and parameters for real-time data retrieval and analysis.
    </td>
  </tr>
  <tr>
    <td width="20%" align="center">
      <img src="https://img.shields.io/badge/4-Data_Retrieval-green?style=for-the-badge&logo=database&logoColor=white" alt="Step 4">
    </td>
    <td width="80%">
      <strong>Market Data Integration</strong><br>
      Secure API calls to RapidAPI services for real-time market data and financial metrics.
    </td>
  </tr>
  <tr>
    <td width="20%" align="center">
      <img src="https://img.shields.io/badge/5-Response_Generation-red?style=for-the-badge&logo=message-square&logoColor=white" alt="Step 5">
    </td>
    <td width="80%">
      <strong>Professional Analysis</strong><br>
      Wall Street-grade insights generated with decisive recommendations and data-driven rationale.
    </td>
  </tr>
</table>

---

<div align="center">
  
### 🌟 Experience the Future of Financial Intelligence

<a href="https://finbee-ai-agent.vercel.app/" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/🚀_Launch_Finbee_AI-FF6B6B?style=for-the-badge&logo=rocket&logoColor=white&labelColor=4ECDC4" alt="Launch Finbee AI" height="60">
</a>

<br><br>

<img src="https://img.shields.io/badge/Made_with_❤️_by-Finbee_Team-orange?style=for-the-badge&logoColor=white" alt="Made with love">

</div>

---

<div align="center">
  <sub>Built with cutting-edge AI technology for professional traders and investors worldwide</sub>
</div>
