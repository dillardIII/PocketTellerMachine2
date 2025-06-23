# === FILE: replit.nix ===
# Replit Build Configuration – Ensures Flask is installed for Python 3.11

{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.flask
  ];
}