from flask import Flask, request, jsonify
from flask_cors import CORS
from model import translate_text

app = Flask(__name__)
CORS(app)   # VERY IMPORTANT

@app.route("/")
def home():
    return "AI Translator Backend is Running!"

@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    text = data["text"]
    result = translate_text(text)
    return jsonify({"translated_text": result})

if __name__ == "__main__":
    app.run(debug=True)
