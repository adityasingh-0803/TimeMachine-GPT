from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    messages = data.get("messages", [])
    profile = data.get("profile", {})

    question = messages[-1]["content"]

    prompt = f"""
You are the user's future self, 10 years older and wiser.

Speak with insight and empathy. Here's your past profile:
Name: {profile.get('name')}
Age: {profile.get('age')}
Goals: {', '.join(profile.get('goals', []))}
Values: {', '.join(profile.get('values', []))}
Fears: {', '.join(profile.get('fears', []))}

They asked: "{question}"

Now respond as their future self:
"""

    ollama_response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )

    reply = ollama_response.json()["response"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
