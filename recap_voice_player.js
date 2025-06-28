// recap_voice_player.js
// Purpose: Load and play voice recap MP3s from /memory/recaps/
// Works with trade results, assistant mood, and persona info

function playRecap(filename, persona, mood) {
  const container = document.getElementById("recapPlayer");
  container.innerHTML = "";

  const label = document.createElement("div");
  label.innerText = `🎙️ ${persona} (${mood}):`;
  label.style.fontWeight = "bold";
  label.style.marginBottom = "0.5rem";

  const audio = document.createElement("audio");
  audio.controls = true;
  audio.autoplay = true;

  const source = document.createElement("source");
  source.src = `/memory/recaps/${filename}`;
  source.type = "audio/mpeg";

  audio.appendChild(source);
  container.appendChild(label);
  container.appendChild(audio);
}

function listAvailableRecaps() {
  fetch('/api/list_recaps')
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById("recapList");
      list.innerHTML = "";

      data.recaps.forEach(r => {
        const button = document.createElement("button");
        button.innerText = `${r.persona} (${r.mood})`;
        button.onclick = () => playRecap(r.filename, r.persona, r.mood);
        list.appendChild(button);
      });
    });
}

// Run on page load if applicable
document.addEventListener("DOMContentLoaded", () => {
  if (document.getElementById("recapList")) {
    listAvailableRecaps();
  }
});