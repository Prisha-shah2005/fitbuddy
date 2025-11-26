from typing import List, Dict, Any
import random


class WorkoutAgent:
    """
    Generates a simple full-body workout based on:
      - fitness_level: beginner / intermediate / advanced
      - goal: fat_loss / muscle_gain / general_fitness
    """

    EXERCISE_DB: List[Dict[str, Any]] = [
        # bodyweight
        {"name": "Bodyweight Squats", "muscle": "Legs", "type": "strength"},
        {"name": "Push-Ups", "muscle": "Chest", "type": "strength"},
        {"name": "Glute Bridges", "muscle": "Glutes", "type": "strength"},
        {"name": "Plank", "muscle": "Core", "type": "core"},
        {"name": "Mountain Climbers", "muscle": "Full Body", "type": "cardio"},
        {"name": "Jumping Jacks", "muscle": "Full Body", "type": "cardio"},
        {"name": "Lunges", "muscle": "Legs", "type": "strength"},
        {"name": "Superman Hold", "muscle": "Back", "type": "core"},
    ]

    def generate_workout(
        self,
        fitness_level: str,
        goal: str,
    ) -> List[Dict[str, Any]]:
        """
        Returns a list of exercises with sets/reps or time.
        """
        level = fitness_level.lower()
        goal = goal.lower()

        # base volume by level
        if level == "beginner":
            sets = 2
            reps = 10
            duration_sec = 30
        elif level == "intermediate":
            sets = 3
            reps = 12
            duration_sec = 40
        else:  # advanced
            sets = 4
            reps = 15
            duration_sec = 45

        # choose 5 random exercises
        exercises = random.sample(self.EXERCISE_DB, k=5)

        plan: List[Dict[str, Any]] = []
        for ex in exercises:
            if ex["type"] == "cardio":
                plan.append(
                    {
                        "name": ex["name"],
                        "muscle": ex["muscle"],
                        "type": ex["type"],
                        "sets": sets,
                        "duration_sec": duration_sec,
                        "reps": None,
                    }
                )
            else:
                # adjust reps a bit based on goal
                goal_reps = reps
                if goal == "fat_loss":
                    goal_reps += 2
                elif goal == "muscle_gain":
                    goal_reps -= 2 if reps > 8 else 0

                plan.append(
                    {
                        "name": ex["name"],
                        "muscle": ex["muscle"],
                        "type": ex["type"],
                        "sets": sets,
                        "reps": goal_reps,
                        "duration_sec": None,
                    }
                )

        return plan
