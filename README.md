🌍 AI Language Translator using Deep Learning

A modern AI-powered language translator built using Deep Learning, Flask backend, and React frontend with a beautiful UI.

🚀 Project Overview

This project translates text from English to other languages using deep learning models from Hugging Face Transformers.

It includes:

🔹 Python Flask Backend

🔹 Deep Learning Translation Model

🔹 React Frontend

🔹 Modern UI Design (Tailwind CSS)

🔹 REST API Integration

🛠️ Tech Stack
Backend:

Python

Flask

Hugging Face Transformers

PyTorch

Frontend:

React.js

Axios

Tailwind CSS

📂 Project Structure
AI_Translator_Project/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── package.json
│
└── README.md

⚙️ Installation Guide
1️⃣ Clone the Repository
git clone <your-repo-link>
cd AI_Translator_Project

🧠 Backend Setup
Step 1: Create Virtual Environment
python -m venv venv


Activate virtual environment:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

Step 2: Install Dependencies
pip install -r requirements.txt


If requirements.txt does not exist, install manually:

pip install flask transformers torch flask-cors

Step 3: Run Backend Server
python app.py


You should see:

AI Translator Backend is Running!


Backend runs on:

http://127.0.0.1:5000

💻 Frontend Setup
Step 1: Navigate to Frontend Folder
cd frontend

Step 2: Install Node Dependencies
npm install

Step 3: Start React App
npm start


Frontend runs on:

http://localhost:3000
