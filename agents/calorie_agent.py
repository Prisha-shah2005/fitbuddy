from typing import List, Dict, Any


class CalorieAgent:
    """
    Rough calorie estimation using MET values:
    calories = MET * weight_kg * duration_hours
    """

    MET_VALUES = {
        "Bodyweight Squats": 5.0,
        "Push-Ups": 8.0,
        "Glute Bridges": 4.0,
        "Plank": 3.0,
        "Mountain Climbers": 8.0,
        "Jumping Jacks": 8.0,
        "Lunges": 5.0,
        "Superman Hold": 3.0,
    }

    def estimate_calories(
        self,
        workout_plan: List[Dict[str, Any]],
        weight_kg: float,
    ) -> float:
        total_calories = 0.0

        for ex in workout_plan:
            name = ex["name"]
            met = self.MET_VALUES.get(name, 5.0)

            if ex["type"] == "cardio":
                # sets * duration_sec each
                duration_min = (ex["sets"] * ex["duration_sec"]) / 60.0
            else:
                # approximate: 45 seconds per set
                duration_min = (ex["sets"] * 45) / 60.0

            duration_hr = duration_min / 60.0
            calories = met * weight_kg * duration_hr
            total_calories += calories

        return round(total_calories, 1)
