# Task-2-Zeotap
Install Dependencies 
# Backend 
cd backend 
pip install -r requirements.txt  
# Frontend
cd ../frontend 
npm install 

Run Locally 
# Start Backend 
cd backend 
uvicorn api:app --reload  
# Start Frontend 
cd frontend 
npm start


📌 README.md

# 📢 CDP Support Chatbot

## 🔥 Overview
A chatbot that answers "how-to" questions for Segment, mParticle, Lytics, and Zeotap using official documentation.

## 📌 Features
✅ Retrieve answers from official CDP docs  
✅ Supports variations in question phrasing  
✅ Cross-CDP comparisons (Bonus)  
✅ FastAPI + React stack  

## 🚀 Tech Stack
- **Frontend:** React.js
- **Backend:** FastAPI (Python)
- **Data Retrieval:** BeautifulSoup, FAISS, Sentence Transformers
- **Deployment:** Vercel (Frontend), Railway (Backend)

## 📖 Setup
### 1️⃣ Clone Repo
```sh
git clone https://github.com/Greeshmalikithareddy2004/cdp-chatbot.git
cd cdp-chatbot
