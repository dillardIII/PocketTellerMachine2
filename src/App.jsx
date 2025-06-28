// === FILE: src/App.jsx === // GhostShare Alpha dApp Frontend (React + Ethers.js)

import { useEffect, useState } from "react"; import { ethers } from "ethers"; import "./App.css";

const CONTRACT_ADDRESS = "<DEPLOYED_CONTRACT_ADDRESS_HERE>"; const CONTRACT_ABI = [ { "inputs": [], "name": "name", "outputs": [{ "internalType": "string", "name": "", "type": "string" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "symbol", "outputs": [{ "internalType": "string", "name": "", "type": "string" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "totalSupply", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "balanceOf", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "_to", "type": "address" }, { "internalType": "uint256", "name": "_value", "type": "uint256" } ], "name": "transfer", "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }], "stateMutability": "nonpayable", "type": "function" } ];

function App() { const [walletAddress, setWalletAddress] = useState(null); const [tokenName, setTokenName] = useState(""); const [tokenSymbol, setTokenSymbol] = useState(""); const [balance, setBalance] = useState(0);

async function connectWallet() { if (window.ethereum) { const accounts = await window.ethereum.request({ method: "eth_requestAccounts" }); setWalletAddress(accounts[0]); } }

async function fetchTokenData() { if (!walletAddress) return; const provider = new ethers.providers.Web3Provider(window.ethereum); const contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, provider); setTokenName(await contract.name()); setTokenSymbol(await contract.symbol()); const bal = await contract.balanceOf(walletAddress); setBalance(ethers.utils.formatUnits(bal, 18)); }

useEffect(() => { if (walletAddress) { fetchTokenData(); } }, [walletAddress]);

return ( <div className="App"> <h1>GhostShare Alpha dApp</h1> {!walletAddress ? ( <button onClick={connectWallet}>Connect MetaMask</button> ) : ( <div> <p>Wallet: {walletAddress}</p> <p>Token: {tokenName} ({tokenSymbol})</p> <p>Balance: {balance}</p> </div> )} </div> ); }

export default App;

