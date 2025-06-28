"""
Dream Network Syncer:
Synchronizes dream-originated concepts and symbolic memory across devices in GhostBridge.
Useful for aligning subconscious logic and AI-processed intuition across PTM nodes.
"""

import os
import json
from datetime import datetime

DREAM_SYNC_LOG = "memory/dream_network_log.json"
DEVICES = ["z_fold_6", "s10", "predator", "slate_7", "steamdeck", "muse_s", "tp_link", "deeper_connect_mini", "flipperzero"]

def load_local_dreams(device_id):
    path = f"devices/{device_id}/dream_cache.json"
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        try:
            return json.load(f)
        except:
            return {}

def merge_dreams(dream_pools):
    unified = {}
    for dreamset in dream_pools:
        for symbol, meaning in dreamset.items():
            if symbol not in unified:
                unified[symbol] = meaning
            else:
                if unified[symbol] != meaning:
                    unified[symbol] += f" / {meaning}"
    return unified

def save_merged_dreams(merged):
    with open(DREAM_SYNC_LOG, "w") as f:
        json.dump({
            "timestamp": datetime.utcnow().isoformat(),
            "merged_symbols": merged
        }, f, indent=2)

def sync_dream_network():
    dream_pools = [load_local_dreams(dev) for dev in DEVICES]
    merged = merge_dreams(dream_pools)
    save_merged_dreams(merged)
    print(f"[DreamNetworkSyncer] Synced {len(merged)} dream-symbol entries across {len(DEVICES)} devices.")