from typing import Dict, Any
from storage.memory_service import MemoryService
from agents.orchestrator_agent import OrchestratorAgent


def print_line():
    print("-" * 50)


def show_profile(profile: Dict[str, Any]) -> None:
    print_line()
    print("👤 Current Profile:")
    print(f"Name           : {profile.get('name')}")
    print(f"Weight (kg)    : {profile.get('weight_kg')}")
    print(f"Fitness Level  : {profile.get('fitness_level')}")
    print(f"Goal           : {profile.get('goal')}")
    print_line()


def setup_profile(memory: MemoryService) -> None:
    print_line()
    print("🔧 Set up / Update Profile")
    name = input("Your name: ").strip() or "Athlete"
    while True:
        try:
            weight_kg = float(input("Your weight (kg): ").strip())
            break
        except ValueError:
            print("Please enter a valid number for weight.")

    print("Fitness level options: beginner / intermediate / advanced")
    fitness_level = input("Your fitness level: ").strip().lower() or "beginner"
    if fitness_level not in ["beginner", "intermediate", "advanced"]:
        fitness_level = "beginner"

    print("Goal options: fat_loss / muscle_gain / general_fitness")
    goal = input("Your goal: ").strip().lower() or "general_fitness"
    if goal not in ["fat_loss", "muscle_gain", "general_fitness"]:
        goal = "general_fitness"

    memory.set_profile(
        name=name,
        weight_kg=weight_kg,
        fitness_level=fitness_level,
        goal=goal,
    )
    print("✅ Profile saved!")


def show_workout(orchestrator: OrchestratorAgent, memory: MemoryService) -> None:
    if not memory.has_profile():
        print("You need to set up your profile first.")
        setup_profile(memory)

    result = orchestrator.generate_daily_workout()

    profile = result["profile"]
    plan = result["workout_plan"]
    calories = result["estimated_calories"]

    show_profile(profile)

    print("💪 Today's Workout Plan")
    print_line()
    for idx, ex in enumerate(plan, start=1):
        if ex["type"] == "cardio":
            print(
                f"{idx}. {ex['name']} ({ex['muscle']}) - "
                f"{ex['sets']} sets x {ex['duration_sec']} sec"
            )
        else:
            print(
                f"{idx}. {ex['name']} ({ex['muscle']}) - "
                f"{ex['sets']} sets x {ex['reps']} reps"
            )
    print_line()
    print(f"Estimated calories burned: {calories} kcal")
    print_line()

    # Ask if user completed and save
    done = input("Did you complete this workout? (y/n): ").strip().lower()
    if done == "y":
        difficulty = input("How difficult was it? (easy/ok/hard): ").strip().lower()
        notes = input("Any notes about today? (optional): ").strip()
        orchestrator.save_today_workout(
            total_calories=calories,
            difficulty=difficulty or "ok",
            notes=notes,
        )
        print("✅ Workout saved to your history!")
    else:
        print("No worries. Come back when you're ready! 🙂")


def show_progress(orchestrator: OrchestratorAgent) -> None:
    data = orchestrator.get_progress_and_motivation()
    progress = data["progress"]
    msg = data["motivation"]

    print_line()
    print("📈 Your Progress Summary")
    print(f"Total workouts : {progress['total_workouts']}")
    print(f"Total calories : {progress['total_calories']} kcal")
    print(f"Average / workout: {progress['average_calories']} kcal")
    print(f"Last workout   : {progress['last_workout_date']}")
    print_line()
    print("💬 Motivation:")
    print(msg)
    print_line()


def main() -> None:
    memory = MemoryService()
    orchestrator = OrchestratorAgent(memory)

    while True:
        print("\n=== FitBuddy – AI Fitness Coach ===")
        print("1. Set / Update Profile")
        print("2. Generate Today's Workout")
        print("3. View Progress & Motivation")
        print("4. Exit")
        choice = input("Choose an option [1-4]: ").strip()

        if choice == "1":
            setup_profile(memory)
        elif choice == "2":
            show_workout(orchestrator, memory)
        elif choice == "3":
            show_progress(orchestrator)
        elif choice == "4":
            print("See you next session! 🏋️‍♂️")
            break
        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
