// === Dashboard Mood Feed Renderer ===

// Load and render mood feed data into the container
function loadDashboardMoodFeed() {
    fetch('/api/get_mood_feed')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('moodFeedContainer');
            if (!container) {
                console.warn("[DashboardMoodFeed] moodFeedContainer not found.");
                return;
            }

            if (!data.length) {
                container.innerHTML = "<p style='color: #888;'>No mood entries yet.</p>";
                return;
            }

            container.innerHTML = data.reverse().map(entry => {
                const time = new Date(entry.timestamp).toLocaleString();
                return `
                    <div style="margin-bottom: 10px;">
                        <strong style="color: #6fd672;">[${entry.persona.toUpperCase()}]</strong>
                        <span style="color: #ccc;">(${entry.mood.toUpperCase()})</span><br>
                        <span style="color: #eee;">"${entry.quote}"</span>
                        <div style="font-size: 12px; color: #555;">${time}</div>
                    </div>
                `;
            }).join('');
        })
        .catch(err => {
            console.error("[DashboardMoodFeed] Error loading feed:", err);
            const container = document.getElementById('moodFeedContainer');
            if (container) {
                container.innerHTML = "<p style='color: #f66;'>Error loading mood feed.</p>";
            }
        });
}

// === Mood Feed Auto-refresh every 30 seconds ===
setInterval(loadDashboardMoodFeed, 30000);

// === Initial Mood Feed Load on page load ===
window.addEventListener("DOMContentLoaded", loadDashboardMoodFeed);