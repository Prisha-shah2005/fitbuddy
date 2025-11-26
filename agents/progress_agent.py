from typing import Dict, Any
from storage.memory_service import MemoryService


class ProgressAgent:
    """
    Reads workout history and computes simple progress stats.
    """

    def __init__(self, memory: MemoryService) -> None:
        self.memory = memory

    def get_progress_summary(self) -> Dict[str, Any]:
        summary = self.memory.get_summary()
        history = self.memory.get_history()

        if not history:
            avg_calories = 0
        else:
            avg_calories = summary["total_calories"] / summary["total_workouts"]

        return {
            "total_workouts": summary["total_workouts"],
            "total_calories": round(summary["total_calories"], 1),
            "average_calories": round(avg_calories, 1),
            "last_workout_date": summary["last_workout_date"],
        }
