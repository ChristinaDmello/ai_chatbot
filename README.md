# Flask ChatBot

A simple chatbot web application built using Flask, HTML, CSS, and JavaScript. The chatbot responds to predefined user messages and stores chat history during the session.

## 🚀 Features

* Simple and clean chatbot interface
* Predefined chatbot responses
* Session-based chat history
* Clear chat functionality
* Built with Flask for backend processing

## 🛠️ Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript

## 📁 Project Structure

```text
project/
│
├── app.py
├── .gitignore
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
└── .venv/ (ignored)

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>

### 2. Navigate to the project folder

```bash
cd flask-chatbot

### 3. Create and activate a virtual environment

```bash
python -m venv .venv

### 4. Install Flask

```bash
pip install flask

### 5. Run the application

```bash
python app.py

### 6. Open your browser and visit

http://127.0.0.1:5000

## 💡 How It Works

* Users enter messages through the chatbot interface.
* Flask processes the messages.
* The chatbot matches user input with predefined responses.
* Responses are displayed instantly in the chat window.
* Chat history is stored temporarily using Flask sessions.

## 🔮 Future Improvements

* AI-powered responses
* Database integration
* User authentication
* Better UI/UX
* Chat history persistence
