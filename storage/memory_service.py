import json
from pathlib import Path
from typing import Any, Dict, List, Optional
import datetime


class MemoryService:
    """
    Very simple JSON-based storage for:
      - user profile (weight, goal, level)
      - workout history (date, total_calories, difficulty, notes)
    """

    def __init__(self, path: str = "fitbuddy_memory.json") -> None:
        self.path = Path(path)
        self.state: Dict[str, Any] = {
            "profile": {
                "name": None,
                "weight_kg": None,
                "fitness_level": None,
                "goal": None,
            },
            "history": [],
        }
        self._load()

    def _load(self) -> None:
        if self.path.exists():
            try:
                self.state = json.loads(self.path.read_text(encoding="utf-8"))
            except Exception:
                # If corrupted, start fresh
                self.state = {
                    "profile": {
                        "name": None,
                        "weight_kg": None,
                        "fitness_level": None,
                        "goal": None,
                    },
                    "history": [],
                }

    def _save(self) -> None:
        self.path.write_text(json.dumps(self.state, indent=2), encoding="utf-8")

    # -------- Profile --------

    def set_profile(
        self,
        name: str,
        weight_kg: float,
        fitness_level: str,
        goal: str,
    ) -> None:
        self.state["profile"] = {
            "name": name,
            "weight_kg": weight_kg,
            "fitness_level": fitness_level,
            "goal": goal,
        }
        self._save()

    def get_profile(self) -> Dict[str, Any]:
        return self.state.get("profile", {})

    def has_profile(self) -> bool:
        p = self.get_profile()
        return bool(p.get("name") and p.get("weight_kg") and p.get("fitness_level"))

    # -------- History --------

    def add_workout_entry(
        self,
        total_calories: float,
        difficulty: str,
        notes: Optional[str] = None,
    ) -> None:
        today = datetime.date.today().isoformat()
        self.state["history"].append(
            {
                "date": today,
                "total_calories": total_calories,
                "difficulty": difficulty,
                "notes": notes or "",
            }
        )
        # keep only last 60 entries
        self.state["history"] = self.state["history"][-60:]
        self._save()

    def get_history(self) -> List[Dict[str, Any]]:
        return self.state.get("history", [])

    def get_summary(self) -> Dict[str, Any]:
        history = self.get_history()
        total_workouts = len(history)
        total_calories = sum(h.get("total_calories", 0) for h in history)
        last_workout = history[-1]["date"] if history else None
        return {
            "total_workouts": total_workouts,
            "total_calories": total_calories,
            "last_workout_date": last_workout,
        }
