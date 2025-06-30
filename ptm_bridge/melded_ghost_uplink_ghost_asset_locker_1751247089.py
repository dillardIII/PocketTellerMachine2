# Auto-rebuilt by GhostForge

# === MELD BREAK ===
        timestamp = datetime.utcnow().isoformat()
        entry = {"timestamp": timestamp, "message": message}
        self.log.append(entry)
        self._save_assets()
        print(f"[GhostLocker] {message}")

    def add_asset(self, category, asset_id, description, metadata=None):
        if category not in self.assets:
            self.log_event(f"⚠️ Unknown asset category: {category}")
            return
        self.assets[category][asset_id] = {
            "description": description,
            "metadata": metadata or {},
            "added": datetime.utcnow().isoformat()
        }
        self.log_event(f"🔐 Added new {category}: {asset_id}")
        self._save_assets()

    def list_assets(self, category=None):
        if category:
            return self.assets.get(category, {})
        return self.assets

    def show_summary(self):
        self.log_event("📦 Displaying asset summary:")
        for cat, items in self.assets.items():
            print(f"\n🗂️ {cat.upper()}: {len(items)} item(s)")
            for key, data in items.items():
                print(f" - {key}: {data['description']}")

# === Entrypoint ===
if __name__ == "__main__":
    locker = GhostAssetLocker()
    locker.show_summary()