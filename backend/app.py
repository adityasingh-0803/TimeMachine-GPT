from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app)

model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    name = data.get("name", "Someone")
    age = data.get("age", "?")
    goals = data.get("goals", "unknown goals")
    values = data.get("values", "unknown values")
    fears = data.get("fears", "unknown fears")
    question = data.get("question", "")
    tone = data.get("tone", "motivational").lower()

    tone_prompt_map = {
        "motivational": "in a motivational tone",
        "poetic": "in a poetic style",
        "funny": "with a humorous tone",
        "formal": "in a professional and formal tone"
    }

    tone_instruction = tone_prompt_map.get(tone, "in a motivational tone")

    prompt = (
        f"Imagine you're the future version of {name}, now {age} years old. "
        f"You've successfully achieved these goals: {goals}. "
        f"You've conquered fears such as: {fears}. "
        f"You live by values: {values}. "
        f"Now, your past self asks: \"{question}\". "
        f"As the wiser version of yourself, offer heartfelt advice, encouragement, and guidance {tone_instruction}."
    )

    result = pipe(prompt, max_new_tokens=150)[0]['generated_text']
    return jsonify({"reply": result})

if __name__ == "__main__":
    app.run(debug=True)
