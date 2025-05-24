// === Assistant Reactions Engine ===

// === Mood Reaction Trigger ===
function triggerAssistantReaction(eventType, outcome = 'neutral') {
    // Example: eventType = 'market_scan', outcome = 'win' | 'loss' | 'neutral'

    // Display related quote
    showAssistantQuote(eventType);

    // Trigger mood quote based on outcome if relevant
    if (['win', 'loss', 'neutral'].includes(outcome)) {
        showMoodQuote(outcome);
    }

    // Update visual mood indicator (optional enhancement)
    updateMoodVisual(outcome);
}

// === Mood Visual Feedback (Optional) ===
function updateMoodVisual(mood) {
    const moodBox = document.getElementById('assistantMoodBox');
    if (!moodBox) return;

    moodBox.classList.remove('win', 'loss', 'neutral');
    moodBox.classList.add(mood);

    // Add slight animation feedback
    moodBox.style.animation = 'pop 0.5s ease';
    setTimeout(() => { moodBox.style.animation = ''; }, 500);
}

// === Pop Animation Keyframes (injects into page dynamically) ===
const popAnimation = document.createElement('style');
popAnimation.innerHTML = `
@keyframes pop {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}
`;
document.head.appendChild(popAnimation);

// === Example Bindings (Simulate Reaction Buttons) ===
function simulateResult(winLossNeutral) {
    triggerAssistantReaction('results_refresh', winLossNeutral);
}

function simulateMarketScan() {
    triggerAssistantReaction('market_scan');
}

function simulateTaskRefresh() {
    triggerAssistantReaction('task_refresh');
}

function simulateBrainCheck() {
    triggerAssistantReaction('brain_check');
}

// === Expose functions globally if needed ===
window.triggerAssistantReaction = triggerAssistantReaction;
window.simulateResult = simulateResult;
window.simulateMarketScan = simulateMarketScan;
window.simulateTaskRefresh = simulateTaskRefresh;
window.simulateBrainCheck = simulateBrainCheck;