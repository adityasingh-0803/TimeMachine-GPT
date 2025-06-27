document.addEventListener("DOMContentLoaded", () => {
  const app = document.getElementById("app");
  app.innerHTML = `
    <h1>⏰ Talk to Your Future Self</h1>
    <p>Fill in your profile and ask a question. Let future-you guide you.</p>
    <input placeholder="Name" id="name">
    <input placeholder="Age" id="age">
    <input placeholder="Your goals" id="goals">
    <input placeholder="Your values" id="values">
    <input placeholder="Your fears" id="fears">
    <select id="tone">
      <option value="motivational">Motivational</option>
      <option value="poetic">Poetic</option>
      <option value="funny">Funny</option>
      <option value="formal">Formal</option>
    </select>
    <textarea placeholder="What do you want to ask future-you?" id="question"></textarea>
    <button id="ask">Ask Future You</button>
    <button id="toggle-voice">🔊 Mute/Unmute Voice</button>
    <div id="response"></div>
  `;

  let isVoiceEnabled = true;
  document.getElementById("toggle-voice").addEventListener("click", () => {
    isVoiceEnabled = !isVoiceEnabled;
  });

  document.getElementById("ask").addEventListener("click", async () => {
    const payload = {
      name: document.getElementById("name").value,
      age: document.getElementById("age").value,
      goals: document.getElementById("goals").value,
      values: document.getElementById("values").value,
      fears: document.getElementById("fears").value,
      question: document.getElementById("question").value,
      tone: document.getElementById("tone").value
    };

    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    document.getElementById("response").innerText = data.reply;

    if (isVoiceEnabled) {
      const utterance = new SpeechSynthesisUtterance(data.reply);
      speechSynthesis.speak(utterance);
    }
  });
});
