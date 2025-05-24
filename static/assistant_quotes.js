// === Assistant Persona Quotes ===
const assistantQuotes = {
    mo_cash: {
        brain_check: ["Let’s see if the brain’s still cooking.", "Mo Cash coming in hot, checking systems!"],
        market_scan: ["Scanning for them money moves.", "Gotta sniff out them winners, scanning now."],
        task_refresh: ["Queue up them tasks, let’s hustle.", "Refreshing the grind, stay sharp."],
        results_refresh: ["Show me the numbers, let’s get paid.", "Results time, baby."]
    },
    mentor: {
        brain_check: ["Let's verify the system's clarity.", "Ensuring Cole's mind is sharp and steady."],
        market_scan: ["Analyzing the market landscape now.", "Scanning for optimal trading opportunities."],
        task_refresh: ["Refreshing task flow for peak efficiency.", "Reassessing objectives, one step at a time."],
        results_refresh: ["Reviewing recent outcomes for insights.", "Time to reflect on our trading results."]
    },
    drill_instructor: {
        brain_check: ["Checking Cole's brain! Snap to attention!", "Status report incoming, stand by!"],
        market_scan: ["Scanning the field, stay frosty!", "Eyes on the market, no slacking!"],
        task_refresh: ["Refreshing the queue, let’s move it!", "Keep that pipeline moving, marine!"],
        results_refresh: ["Results incoming, prepare for debrief!", "Reviewing performance, no excuses!"]
    },
    comedian: {
        brain_check: ["Let’s poke Cole’s brain—gently. Maybe.", "Is this thing on? Brain check in progress!"],
        market_scan: ["Scanning the market... like a nosy neighbor.", "Let’s see who’s making bad trades today."],
        task_refresh: ["Refreshing tasks. Because, you know, work.", "Hitting refresh like it owes me money."],
        results_refresh: ["Results time! Don’t shoot the messenger.", "Let’s see how bad or good we did."]
    }
};

// === Play Assistant Voice ===
function playAssistantVoice(persona, event) {
    const voiceFile = `/static/audio/${persona}_${event}.mp3`;
    const audio = new Audio(voiceFile);
    audio.play().catch(e => console.error("Voice playback error:", e));
}

// === Display Quote + Play Voice ===
function showAssistantQuote(event) {
    const persona = localStorage.getItem('active_persona') || 'mo_cash';
    const quotes = assistantQuotes[persona]?.[event] || [];
    if (quotes.length === 0) return;

    const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
    const quoteBox = document.getElementById('assistantQuoteBox');
    if (quoteBox) {
        quoteBox.innerText = randomQuote;
    }

    playAssistantVoice(persona, event);
}

// === Unified Command Functions with Voice Synced Quotes ===

function checkBrain() {
    fetch('/api/cole_think_test')
        .then(res => res.json())
        .then(data => {
            document.getElementById('brainStatus').innerText = data.response;
            showAssistantQuote('brain_check');
        })
        .catch(err => {
            document.getElementById('brainStatus').innerText = "Error: " + err;
        });
}

function scanMarket() {
    document.getElementById('marketLog').innerText = "Scanning...";
    fetch('/api/cole_market_scan')
        .then(res => res.json())
        .then(data => {
            document.getElementById('marketLog').innerText = JSON.stringify(data, null, 2);
            showAssistantQuote('market_scan');
        })
        .catch(err => {
            document.getElementById('marketLog').innerText = "Error: " + err;
        });
}

function refreshTasks() {
    fetch('/api/get_tasks')
        .then(res => res.json())
        .then(data => {
            document.getElementById('tasksLog').innerText = JSON.stringify(data, null, 2);
            showAssistantQuote('task_refresh');
        })
        .catch(err => {
            document.getElementById('tasksLog').innerText = "Error: " + err;
        });
}

function refreshResults() {
    fetch('/api/get_results')
        .then(res => res.json())
        .then(data => {
            document.getElementById('resultsLog').innerText = JSON.stringify(data.slice(-5), null, 2);
            showAssistantQuote('results_refresh');
        })
        .catch(err => {
            document.getElementById('resultsLog').innerText = "Error: " + err;
        });
}