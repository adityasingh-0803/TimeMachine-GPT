from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual API key

SYSTEM_PROMPT = """
You are the user's future self, 10 years older, wiser, and emotionally aware.
Speak with empathy, perspective, and clarity. Use details from the user's profile
to make your advice personal and motivating. Always answer as if you're them — from the future.
"""

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    messages = data.get("messages", [])
    profile = data.get("profile", {})

    intro = f"User Profile:\nName: {profile.get('name')}\nAge: {profile.get('age')}\nGoals: {', '.join(profile.get('goals', []))}\nValues: {', '.join(profile.get('values', []))}\nFears: {', '.join(profile.get('fears', []))}"

    gpt_messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": intro},
    ] + messages

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=gpt_messages,
        temperature=0.8
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
