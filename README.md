 🏋️‍♂️ FitBuddy – Your Personal AI Fitness & Workout Coach

FitBuddy is an AI-powered fitness assistant designed to help you build healthy workout habits, stay motivated, and track your progress — all without needing a trainer or gym membership.

This project was built as part of the **Concierge Agents Track**, where the goal is to design intelligent agents that assist individuals with everyday tasks. FitBuddy focuses on **daily fitness**, combining multiple simple AI-driven agents to deliver personalized workout routines and motivational progress tracking.


 🚀 Why FitBuddy?

Many people struggle with:
- knowing which exercises to do  
- staying consistent  
- estimating calories burned  
- tracking long-term progress  
- finding motivation to continue  

FitBuddy solves these problems by acting as a **personal workout planner**, **nutrition-aware calorie estimator**, and **progress coach** — all in one lightweight Python application that runs locally on any machine.



 🔥 Key Features

 🏋️ Personalized Workout Generator
Generates a full-body workout based on:
- your **fitness level** (beginner, intermediate, advanced)
- your **goal** (fat loss, muscle gain, general fitness)
- randomly selected exercises for variety

🔥 Calorie Burn Estimation
Uses MET-based formulas to estimate calories burned for your workout.

📈 Progress Tracking
Automatically logs:
- date of workout
- calories burned
- workout difficulty
- your workout notes

And provides:
- total workouts
- total calories burned
- average calories per workout
- last workout date

 💬 Daily Motivation
FitBuddy reads your progress and gives a simple motivational message designed to keep you moving.

 💾 Local Memory (No Internet Needed)
All data is stored safely in a local JSON file:

┌────────────────────────┐
│     Calorie Agent      │
│ Estimates calories     │
└────────────────────────┘

┌────────────────────────┐
│     Progress Agent     │
│ Tracks and analyzes    │
└────────────────────────┘

┌────────────────────────┐
│    Motivation Agent    │
│ Generates messages     │
└────────────────────────┘

┌────────────────────────┐
│     Memory Service     │
│ JSON-based storage     │
└────────────────────────┘

This architecture makes FitBuddy:

- clean  
- extendable  
- easy to debug  
- easy to add new agents in future  

---

 🗂 Project Structure
fitbuddy/
│ README.md
│ main.py
│
├── agents/
│ ├── workout_agent.py
│ ├── calorie_agent.py
│ ├── progress_agent.py
│ ├── motivation_agent.py
│ └── orchestrator_agent.py
│
└── storage/
└── memory_service.py

=== FitBuddy – AI Fitness Coach ===
1. Set / Update Profile
2. Generate Today's Workout
3. View Progress & Motivation
4. Exit

Generate Today's Workout

FitBuddy creates a custom plan like:

💪 Today's Workout Plan
--------------------------------------------------
1. Push-Ups (Chest) - 3 sets x 12 reps
2. Plank (Core) - 3 sets x 40 sec
3. Lunges (Legs) - 3 sets x 12 reps
...
Estimated calories burned: 162.4 kcal

📈 Your Progress Summary
Total workouts   : 5
Total calories   : 773.2 kcal
Average / workout: 154.6 kcal
Last workout     : 2025-11-26

💬 Motivation:
Solid work! Your average burn is strong. Stay locked in 🧠
