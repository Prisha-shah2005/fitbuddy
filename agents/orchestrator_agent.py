from typing import Dict, Any, List

from storage.memory_service import MemoryService
from agents.workout_agent import WorkoutAgent
from agents.calorie_agent import CalorieAgent
from agents.progress_agent import ProgressAgent
from agents.motivation_agent import MotivationAgent


class OrchestratorAgent:
    """
    High-level controller:
      - uses profile
      - builds workout
      - computes calories
      - saves history
      - returns progress + motivation
    """

    def __init__(self, memory: MemoryService) -> None:
        self.memory = memory
        self.workout_agent = WorkoutAgent()
        self.calorie_agent = CalorieAgent()
        self.progress_agent = ProgressAgent(memory)
        self.motivation_agent = MotivationAgent()

    def generate_daily_workout(self) -> Dict[str, Any]:
        profile = self.memory.get_profile()
        if not profile or not profile.get("weight_kg"):
            raise ValueError("User profile is not set.")

        level = profile["fitness_level"]
        goal = profile["goal"]
        weight = float(profile["weight_kg"])

        workout_plan: List[Dict[str, Any]] = self.workout_agent.generate_workout(
            fitness_level=level,
            goal=goal,
        )

        calories = self.calorie_agent.estimate_calories(workout_plan, weight)

        result = {
            "profile": profile,
            "workout_plan": workout_plan,
            "estimated_calories": calories,
        }

        return result

    def save_today_workout(self, total_calories: float, difficulty: str, notes: str) -> None:
        self.memory.add_workout_entry(
            total_calories=total_calories,
            difficulty=difficulty,
            notes=notes,
        )

    def get_progress_and_motivation(self) -> Dict[str, Any]:
        progress = self.progress_agent.get_progress_summary()
        message = self.motivation_agent.build_message(progress)
        return {
            "progress": progress,
            "motivation": message,
        }
