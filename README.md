# AI-Content-Detector

## Project Overview

The **AI-Content Detector** project aims to detect whether a given text is AI-generated or human-written. The project consists of a web-based interface that allows users to input text and checks the content's authenticity using a pre-trained machine learning model on the backend. The interface responds with a "YES" or "NO" based on the prediction.

### Key Features:
- **Frontend**: Built with React for a responsive and clean user interface.
- **Backend**: Uses Flask and a pre-trained model from Hugging Face's `transformers` library.
- **AI Model**: Based on OpenAI’s Roberta model for AI-content detection.

---

## Requirements

Ensure you have the following installed:
- Python 3.12 or higher
- Node.js and npm
- Virtual Environment (venv)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/KshithijKeshav/ai-content-detector.git
cd ai-content-detector
```

### 2. Run the  Initialization script
**Mac\Linux**
```python
python3 init_project.py
```
**Windows**
```python
python init_win_proj.py
```
### 3.Running the Project
#### 4. Flask server
**Mac\Linux**
```bash
source Backend/backend/bin/activate
```
**Windows**
```bash
Backen\backend\Scripts\activate
```

#### 4a. Run Flask Server
**Mac\Linux**
```bash
cd backend
python3 server.py
```
**Windows**
```bash
cd backend
python server.py
```
#### 5.Run React(Frontend)
```bash
cd frontend
npm start
```
### Make sure your file directory looks like this
```bash
├── backend/                  # Flask API
│   ├── venv/                 # Python virtual environment
│   ├── server.py             # Main Flask server
│   ├── requirements.txt      # Python dependencies
├── frontend/                 # React frontend
│   ├── node_modules/         # Installed Node modules
│   ├── src/                  # React components
│   ├── App.js                # Main React App component
│   ├── package.json          # Node.js dependencies
├── init_project.py           # Python script for initializing project
```
