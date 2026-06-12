from flask import Flask, render_template, request, jsonify, session
import uuid

app = Flask(__name__)
app.secret_key = "chatbot-secret-key-2024"

RESPONSES = {
    "hello": "Hi! How can I help you?",
    "hi": "Hey there! What can I do for you?",
    "how are you": "I'm doing great, thanks for asking!",
    "what is your name": "I'm ChatBot, your friendly assistant!",
    "what can you do": "I can answer simple questions and have a basic conversation with you!",
    "bye": "Goodbye! Have a wonderful day!",
    "goodbye": "See you later! Take care!",
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    "help": "You can say hello, ask how I am, or just chat. I'll do my best to respond!",
}

DEFAULT_RESPONSE = "I'm not sure how to respond to that. Try saying 'help' to see what I can do!"


def get_bot_response(user_message):
    normalized = user_message.lower().strip()
    for key, response in RESPONSES.items():
        if key in normalized:
            return response
    return DEFAULT_RESPONSE


@app.route("/")
def index():
    if "chat_history" not in session:
        session["chat_history"] = []
    return render_template("index.html", chat_history=session["chat_history"])


@app.route("/send", methods=["POST"])
def send_message():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    bot_reply = get_bot_response(user_message)

    if "chat_history" not in session:
        session["chat_history"] = []

    session["chat_history"].append({"sender": "user", "text": user_message})
    session["chat_history"].append({"sender": "bot", "text": bot_reply})
    session.modified = True

    return jsonify({"reply": bot_reply})


@app.route("/clear", methods=["POST"])
def clear_history():
    session["chat_history"] = []
    session.modified = True
    return jsonify({"status": "cleared"})


if __name__ == "__main__":
    app.run(debug=True)
