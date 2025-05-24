// ghost_commands.js

// === Ghost Command Parser ===
// Accepts voice or text and maps to PTM functions

const GhostCommands = {
  parse(input) {
    const text = input.toLowerCase().trim();

    // === Quick Matches ===
    if (text.includes("trigger trade") || text.includes("run trade")) {
      return { action: "trigger_autotrade", message: "Running autotrade now..." };
    }

    if (text.includes("show my trades") || text.includes("trade history")) {
      return { action: "navigate", target: "/trade_dashboard", message: "Opening trade dashboard..." };
    }

    if (text.includes("show my profile")) {
      return { action: "navigate", target: "/profile_stats", message: "Opening your profile now..." };
    }

    if (text.includes("start quiz") || text.includes("take a quiz")) {
      return { action: "navigate", target: "/quiz_live_session", message: "Loading quiz session..." };
    }

    if (text.includes("battle mode") || text.includes("start battle")) {
      return { action: "navigate", target: "/battle_room", message: "Launching Battle Room!" };
    }

    if (text.includes("command center")) {
      return { action: "navigate", target: "/command_center", message: "Opening Command Center..." };
    }

    if (text.includes("show alerts") || text.includes("group alerts")) {
      return { action: "navigate", target: "/group_alert_feed", message: "Opening Group Alert Feed..." };
    }

    if (text.includes("strategy") && text.includes("builder")) {
      return { action: "navigate", target: "/strategy_builder", message: "Opening Strategy Builder..." };
    }

    if (text.includes("game board") || text.includes("dashboard")) {
      return { action: "navigate", target: "/", message: "Returning to PTM Dashboard..." };
    }

    if (text.includes("what's my score") || text.includes("check xp")) {
      return { action: "fetch_stats", message: "Checking XP and performance..." };
    }

    if (text.includes("mentor") || text.includes("mo cash") || text.includes("drill instructor")) {
      return { action: "switch_voice", voice: extractVoiceName(text), message: `Switching to ${extractVoiceName(text)} voice.` };
    }

    return { action: "unknown", message: "Command not recognized. Try saying 'trigger trade' or 'show my profile'." };
  }
};

function extractVoiceName(text) {
  if (text.includes("mentor")) return "Mentor";
  if (text.includes("mo cash")) return "Mo Cash";
  if (text.includes("drill instructor")) return "Drill Instructor";
  if (text.includes("strategist")) return "Strategist";
  if (text.includes("optimist")) return "Optimist";
  return "Default";
}

// === Export (if using module) ===
if (typeof module !== "undefined") {
  module.exports = GhostCommands;
}