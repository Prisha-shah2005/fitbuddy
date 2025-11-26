from typing import Dict, Any


class MotivationAgent:
    """
    Very simple rule-based motivational messages.
    """

    def build_message(self, progress: Dict[str, Any]) -> str:
        total = progress["total_workouts"]
        avg_cal = progress["average_calories"]

        if total == 0:
            return "Everyone starts somewhere 💪 Let today be your Day 1!"
        if total < 5:
            return f"Nice start! You’ve completed {total} workouts. Keep the streak going! 🔥"
        if avg_cal < 150:
            return "You're building consistency. Try pushing just a bit harder each session! 🚀"
        if avg_cal < 300:
            return "Solid work! Your average burn is strong. Stay locked in 🧠"
        return "Beast mode activated 😎 Your workouts are on fire. Remember to recover well too!"
