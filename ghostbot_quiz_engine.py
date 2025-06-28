# ghostbot_quiz_engine.py
# Purpose: Quiz engine for GhostBot education module
# Generates multiple-choice quizzes, scores results, tracks grades and XP

import json
import os
from datetime import datetime
from utils.logger import log_event

class GhostBotQuizEngine:
    def __init__(self):
        self.quiz_dir = "memory/quiz_scores/"
        self.current_quiz = []
        self.user_xp = 0

        if not os.path.exists(self.quiz_dir):
            os.makedirs(self.quiz_dir)

    def load_quiz(self, lesson_id):
        """Load quiz data from a lesson source file."""
        quiz_file = f"lessons/{lesson_id}_quiz.json"
        if not os.path.exists(quiz_file):
            raise FileNotFoundError(f"No quiz file found for lesson: {lesson_id}")

        with open(quiz_file, "r") as f:
            self.current_quiz = json.load(f)

        return self.current_quiz

    def score_quiz(self, user_answers, username="user"):
        """Compare user answers and calculate grade + XP."""
        correct = 0
        results = []

        for idx, qa in enumerate(self.current_quiz):
            question = qa["question"]
            correct_answer = qa["answer"]
            user_response = user_answers[idx]

            is_correct = (user_response.strip().lower() == correct_answer.strip().lower())
            if is_correct:
                correct += 1
                self.user_xp += 10  # reward per correct answer

            results.append({
                "question": question,
                "correct_answer": correct_answer,
                "user_answer": user_response,
                "correct": is_correct
            })

        total = len(self.current_quiz)
        percent = (correct / total) * 100

        if percent >= 90:
            grade = "A"
        elif percent >= 80:
            grade = "B"
        elif percent >= 70:
            grade = "C"
        elif percent >= 60:
            grade = "D"
        else:
            grade = "F"

        result_data = {
            "timestamp": str(datetime.now()),
            "user": username,
            "correct": correct,
            "total": total,
            "grade": grade,
            "xp_earned": correct * 10,
            "details": results
        }

        self._save_quiz_result(username, result_data)
        log_event("Quiz Scored", result_data)
        return result_data

    def _save_quiz_result(self, username, data):
        """Save results to user's quiz log."""
        user_file = os.path.join(self.quiz_dir, f"{username}_results.json")
        history = []

        if os.path.exists(user_file):
            with open(user_file, "r") as f:
                history = json.load(f)

        history.append(data)

        with open(user_file, "w") as f:
            json.dump(history, f, indent=4)

    def get_user_xp(self):
        """Return total XP earned during session."""
        return self.user_xp