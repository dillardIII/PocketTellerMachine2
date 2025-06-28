# === FILE: group_review_orchestrator.py ===
import os
from team_file_router import send_file_to_team
from shutil import copyfile

REVIEW_TEAMS = {
    "Cole": ["Strategist", "Mentor", "ChillTrader"],
    "Strategist": ["Cole", "Mentor"],
    "Mentor": ["Cole", "Strategist"],
}

def start_group_review(sender, file_path):
    reviewers = REVIEW_TEAMS.get(sender, [])
    if not reviewers:
        print(f"[GROUP_REVIEW] No reviewers assigned for {sender}.")
        return

    for reviewer in reviewers:
        # Create a separate copy per reviewer to trigger their reaction logic
        review_copy = file_path.replace(".py", f"_{reviewer}_review.py")
        copyfile(file_path, review_copy)

        send_file_to_team(
            sender=sender,
            recipient=reviewer,
            file_path=review_copy,
            description=f"{sender} submitted this for group review."
        )
        print(f"[GROUP_REVIEW] Sent copy to {reviewer}: {review_copy}")