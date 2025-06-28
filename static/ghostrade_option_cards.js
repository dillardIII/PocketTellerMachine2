// ghostrade_option_cards.js
// Purpose: Visual card system to represent and teach options strategies inside PTM
// Each card = one leg of a strategy (Buy Call, Sell Put, etc.)
// Cards can be stacked, explained, and animated in UI

const optionCards = [
  {
    id: "buy_call",
    name: "Buy Call",
    description: "Gives the right to buy the stock at the strike price before expiration.",
    risk: "Limited to premium paid",
    reward: "Unlimited (theoretically)",
    visual: "📈",
    type: "bullish"
  },
  {
    id: "sell_call",
    name: "Sell Call",
    description: "Obligation to sell stock at strike price if assigned.",
    risk: "Unlimited loss if stock rises",
    reward: "Limited to premium received",
    visual: "💸",
    type: "bearish"
  },
  {
    id: "buy_put",
    name: "Buy Put",
    description: "Gives the right to sell the stock at the strike price.",
    risk: "Limited to premium paid",
    reward: "High if stock falls sharply",
    visual: "📉",
    type: "bearish"
  },
  {
    id: "sell_put",
    name: "Sell Put",
    description: "Obligation to buy stock at strike price if assigned.",
    risk: "Large if stock falls",
    reward: "Premium received",
    visual: "💵",
    type: "bullish"
  },
  {
    id: "iron_condor",
    name: "Iron Condor",
    description: "Neutral strategy: Sell OTM Call & Put, Buy further OTM Call & Put.",
    risk: "Limited",
    reward: "Limited",
    visual: "🪶",
    type: "neutral"
  },
  {
    id: "covered_call",
    name: "Covered Call",
    description: "Own stock + Sell Call: generate income while holding stock.",
    risk: "Stock downside",
    reward: "Premium + stock gains up to strike",
    visual: "🛡️",
    type: "neutral"
  },
  {
    id: "credit_spread",
    name: "Credit Spread",
    description: "Sell option closer to the money, buy option further OTM.",
    risk: "Limited to width minus credit",
    reward: "Net premium received",
    visual: "🎯",
    type: "directional"
  }
];

// Function: Render all cards into container
function renderOptionCards(containerId) {
  const container = document.getElementById(containerId);
  container.innerHTML = "";

  optionCards.forEach(card => {
    const div = document.createElement("div");
    div.className = "option-card";

    div.innerHTML = `
      <div class="card-icon">${card.visual}</div>
      <div class="card-title">${card.name}</div>
      <div class="card-type">(${card.type})</div>
      <div class="card-description">${card.description}</div>
      <div class="card-risk"><b>Risk:</b> ${card.risk}</div>
      <div class="card-reward"><b>Reward:</b> ${card.reward}</div>
    `;

    container.appendChild(div);
  });
}

// Function: Stack cards visually
function stackCards(cardIds, containerId) {
  const container = document.getElementById(containerId);
  container.innerHTML = "";

  cardIds.forEach(id => {
    const card = optionCards.find(c => c.id === id);
    if (card) {
      const div = document.createElement("div");
      div.className = "option-card stacked";

      div.innerHTML = `
        <div class="card-icon">${card.visual}</div>
        <div class="card-title">${card.name}</div>
        <div class="card-type">(${card.type})</div>
        <div class="card-description">${card.description}</div>
        <div class="card-risk"><b>Risk:</b> ${card.risk}</div>
        <div class="card-reward"><b>Reward:</b> ${card.reward}</div>
      `;

      container.appendChild(div);
    }
  });
}