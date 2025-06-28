// === FILE: meta_mask_auth.js ===
async function connectMetaMask() {
  if (typeof window.ethereum !== 'undefined') {
    try {
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      const address = accounts[0];
      alert("✅ Connected to MetaMask: " + address);

      // Send to backend (Flask) if needed
      fetch('/store_wallet', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ address })
      });

    } catch (err) {
      alert("❌ MetaMask connection failed: " + err.message);
    }
  } else {
    alert("🦊 MetaMask not found. Please install it.");
  }
}