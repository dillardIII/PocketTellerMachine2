// === Dashboard Mood Triggers ===

// List of moods to trigger for testing
const testMoods = ['win', 'loss', 'neutral'];

// Trigger mood quote and voice
function triggerMood(persona, mood) {
    localStorage.setItem('active_persona', persona);
    showMoodQuote(mood);
}

// Dynamically create mood trigger buttons for UI testing
function renderMoodTriggers() {
    const container = document.getElementById('moodTriggerContainer');
    if (!container) {
        console.warn("[MoodTriggers] moodTriggerContainer not found.");
        return;
    }

    const personas = ['mo_cash', 'mentor', 'drill_instructor', 'comedian'];

    container.innerHTML = personas.map(persona => `
        <div style="margin-bottom: 20px;">
            <h3 style="color: #6fd672;">${persona.replace('_', ' ').toUpperCase()}</h3>
            ${testMoods.map(mood => `
                <button style="margin-right: 10px;" onclick="triggerMood('${persona}', '${mood}')">
                    ${mood.toUpperCase()}
                </button>
            `).join('')}
        </div>
    `).join('');
}

// Initialize Mood Triggers UI after page loads
window.addEventListener("DOMContentLoaded", renderMoodTriggers);