# 🕰️ TimeMachine GPT

An interactive AI chatbot that lets you talk to a **wiser, future version of yourself**. Ask questions, share your fears, and get encouraging, poetic, or honest responses — even spoken out loud! Powered by **Transformers**, **Flask**, and **Text-to-Speech**.

---

## 🧠 Features

- 🎤 Voice-enabled chatbot (Speak/Mute toggle)
- ✍️ Multiple tones: Motivational, Poetic, Honest
- 💬 Personalized responses based on your goals, values, and fears
- 📦 Uses Hugging Face’s `flan-t5-base` model for high-quality text generation

---

## 📁 Project Structure
```bash
timemachine-gpt/
├── backend/
│ ├── app.py # Flask backend + Transformers
│ └── requirements.txt # Python dependencies
└── frontend/
├── index.html # UI layout
├── app.js # Interaction + text-to-speech
└── style.css # Visual styling
```

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/timemachine-gpt.git
cd timemachine-gpt
```
### 2. Set up the backend
```bash
cd backend
python -m venv venv
source venv/bin/activate          # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
### 3. Open the frontend
```bash
http://localhost:5000
```
Fill out the form with your name, age, goals, values, fears, and a question. Choose a tone and ask — your future self will answer!
