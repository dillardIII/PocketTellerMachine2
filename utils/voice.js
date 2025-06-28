function speak(text) {
  const synth = window.speechSynthesis;
  const utter = new SpeechSynthesisUtterance(text);
  utter.pitch = 1;
  utter.rate = 1;
  utter.voice = synth.getVoices().find(v => v.name.includes("Google") || true);
  synth.speak(utter);
}