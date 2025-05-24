<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pocket Teller Machine - Unified Command Center</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        /* (your CSS styles stay exactly as they are) */
    </style>
</head>
<body>
    <header>Pocket Teller Machine - Unified Command Center</header>

    <div class="dashboard-container">

        <!-- Portfolio Overview -->
        <div class="section">
            <h2>Portfolio Overview</h2>
            <p>Your account balance, open positions, and profit/loss summary.</p>
        </div>

        <!-- Trade History -->
        <div class="section">
            <h2>Trade History</h2>
            <p>Recent trades, win/loss ratios, and trade summaries.</p>
        </div>

        <!-- Congress Sections -->
        <div class="section">{% include 'dashboard_congress_section.html' %}</div>
        <div class="section">{% include 'dashboard_congress_widget.html' %}</div>
        <div class="section">{% include 'dashboard_congress_heatmap.html' %}</div>
        <div class="section">{% include 'dashboard_congress_sparklines.html' %}</div>
        <div class="section">{% include 'dashboard_congress_summary.html' %}</div>

        <!-- Assistant Quote Display -->
        <div class="section" style="text-align: center;">
            <h2>Assistant Says:</h2>
            <p id="assistantQuoteBox" style="font-size: 18px; font-style: italic; color: #6fd672;">
                I'm ready to help you hustle.
            </p>
        </div>

        <!-- Unified Command Cards -->
        <div class="grid">
            <div class="card">
                <h2>Brain Status</h2>
                <button onclick="checkBrain()">Check Cole Brain</button>
                <div id="brainStatus">Loading...</div>
            </div>

            <div class="card">
                <h2>Market Scanner</h2>
                <button onclick="scanMarket()">Scan Market Now</button>
                <pre id="marketLog">Waiting...</pre>
            </div>

            <div class="card">
                <h2>Task Queue</h2>
                <button onclick="refreshTasks()">Refresh Queue</button>
                <pre id="tasksLog">Waiting...</pre>
            </div>

            <div class="card">
                <h2>Recent Results</h2>
                <button onclick="refreshResults()">Refresh Results</button>
                <pre id="resultsLog">Waiting...</pre>
            </div>

            <div class="card">
                <h2>Assistant Voice Previews</h2>
                <div class="grid">
                    <div>
                        <div class="avatar" style="background-image: url('/static/avatars/mo_cash_avatar.png');"></div>
                        <button onclick="playVoice('mo_cash')">Mo Cash</button>
                    </div>
                    <div>
                        <div class="avatar" style="background-image: url('/static/avatars/mentor_avatar.png');"></div>
                        <button onclick="playVoice('mentor')">Mentor</button>
                    </div>
                    <div>
                        <div class="avatar" style="background-image: url('/static/avatars/drill_instructor_avatar.png');"></div>
                        <button onclick="playVoice('drill_instructor')">Drill Instructor</button>
                    </div>
                    <div>
                        <div class="avatar" style="background-image: url('/static/avatars/comedian_avatar.png');"></div>
                        <button onclick="playVoice('comedian')">Comedian</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- JS Assets for Mood Quotes & Engine -->
    <script src="/static/js/assistant_mood_quotes.js"></script>
    <script src="/static/js/assistant_mood_engine.js"></script>

    <script>
        // Existing JS functions: checkBrain, scanMarket, refreshTasks, refreshResults, playVoice, etc.
    </script>
</body>
</html>