// === Mood Logger ===
function logMoodEvent(persona, mood, quote) {
    const payload = {
        persona: persona,
        mood: mood,
        quote: quote
    };

    fetch('/api/log_mood_event', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    })
    .then(res => res.json())
    .then(data => {
        console.log("[Mood Logger]", data.message);
        refreshMoodFeed();
    })
    .catch(err => {
        console.error("[Mood Logger] Error:", err);
    });
}

// === Mood Feed Refresh ===
function refreshMoodFeed() {
    fetch('/api/get_mood_feed')
        .then(res => res.json())
        .then(data => {
            const feedContainer = document.getElementById('moodFeedContainer');
            if (!feedContainer) return;

            feedContainer.innerHTML = "";

            data.reverse().forEach(entry => {
                const item = document.createElement('div');
                item.className = 'mood-feed-item';
                item.innerHTML = `
                    <strong>[${entry.persona}]</strong> (${entry.mood}): ${entry.quote}
                    <div class="mood-timestamp">${new Date(entry.timestamp).toLocaleString()}</div>
                `;
                feedContainer.appendChild(item);
            });
        })
        .catch(err => {
            console.error("[Mood Feed] Error loading feed:", err);
        });
}

// === Assistant Mood Logger ===
function logAssistantMood(persona, mood, quote) {
    const payload = {
        persona: persona,
        mood: mood,
        quote: quote
    };

    fetch('/api/log_mood_entry', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            console.log(`[Mood Logger] Logged mood: ${persona} | ${mood} | "${quote}"`);
        } else {
            console.error(`[Mood Logger] Failed to log mood: ${data.message}`);
        }
    })
    .catch(error => {
        console.error(`[Mood Logger] Error logging mood:`, error);
    });
}

// === Mood Logger Hook ===
function moodLoggerHook(persona, mood, quote) {
    logAssistantMood(persona, mood, quote);
}

// === Hook into Existing Mood Quote Trigger ===
function showMoodQuote(mood) {
    const persona = localStorage.getItem('active_persona') || 'mo_cash';
    const quotes = assistantMoodQuotes[persona]?.[mood] || [];
    if (quotes.length === 0) return;

    const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
    const quoteBox = document.getElementById('assistantQuoteBox');
    if (quoteBox) {
        quoteBox.innerText = randomQuote;
    }

    playMoodVoice(persona, mood);
    logMoodEvent(persona, mood, randomQuote);  // Logs to /api/log_mood_event (existing logger)
    moodLoggerHook(persona, mood, randomQuote); // Logs to /api/log_mood_entry (new logger)
}