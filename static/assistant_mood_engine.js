// === Assistant Mood Engine ===

// Current mood state (default is neutral)
let currentMood = 'neutral';

// === Mood State Setter ===
function setMoodState(mood) {
    if (['win', 'loss', 'neutral'].includes(mood)) {
        currentMood = mood;
        console.log(`Mood set to: ${mood}`);
        localStorage.setItem('cole_mood', mood);
        updateMoodDisplay();
    } else {
        console.warn(`Invalid mood state: ${mood}`);
    }
}

// === Load Saved Mood from LocalStorage ===
function loadMoodState() {
    const savedMood = localStorage.getItem('cole_mood');
    if (savedMood && ['win', 'loss', 'neutral'].includes(savedMood)) {
        currentMood = savedMood;
    }
    updateMoodDisplay();
}

// === Update Mood Display in Dashboard ===
function updateMoodDisplay() {
    const moodBox = document.getElementById('assistantQuoteBox');
    if (!moodBox) return;

    switch (currentMood) {
        case 'win':
            moodBox.style.color = '#00FF99';
            break;
        case 'loss':
            moodBox.style.color = '#FF4444';
            break;
        default:
            moodBox.style.color = '#6fd672';
    }
}

// === Mood-Based Quote Override ===
function showMoodBasedQuote(event) {
    const persona = localStorage.getItem('active_persona') || 'mo_cash';
    const moodQuotes = assistantMoodQuotes[persona]?.[currentMood]?.[event] || [];

    if (moodQuotes.length === 0) {
        console.warn(`No mood quotes found for ${persona} in ${currentMood} mood.`);
        return;
    }

    const randomQuote = moodQuotes[Math.floor(Math.random() * moodQuotes.length)];
    const quoteBox = document.getElementById('assistantQuoteBox');
    if (quoteBox) {
        quoteBox.innerText = randomQuote;
    }

    // Play matching mood-based voice file
    playAssistantVoiceMood(persona, event, currentMood);
}

// === Mood-Based Voice Playback ===
function playAssistantVoiceMood(persona, event, mood) {
    const voiceFile = `/static/audio/${persona}_${event}_${mood}.mp3`;
    const audio = new Audio(voiceFile);
    audio.play().catch(e => console.error("Mood voice playback error:", e));
}

// === Mood Trigger Example (for Wins/Losses) ===
function triggerWin() {
    setMoodState('win');
    showMoodBasedQuote('results_refresh');
}

function triggerLoss() {
    setMoodState('loss');
    showMoodBasedQuote('results_refresh');
}

function resetMood() {
    setMoodState('neutral');
    showMoodBasedQuote('results_refresh');
}

// === Initialize Mood Engine on Load ===
document.addEventListener('DOMContentLoaded', loadMoodState);