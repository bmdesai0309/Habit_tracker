# habit_manager.py

import json
import os
from datetime import datetime, timedelta

DATA_FILE = "data/habits_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_habit(habit_name):
    data = load_data()
    if habit_name in data:
        print(f"Habit '{habit_name}' already exists.")
    else:
        data[habit_name] = {"dates_completed": []}
        save_data(data)
        print(f"Habit '{habit_name}' added successfully.")

def mark_habit_completed(habit_name):
    data = load_data()
    today = datetime.today().strftime("%Y-%m-%d")
    
    if habit_name not in data:
        print(f"Habit '{habit_name}' does not exist.")
    else:
        if today in data[habit_name]["dates_completed"]:
            print(f"Habit '{habit_name}' is already marked complete for today.")
        else:
            data[habit_name]["dates_completed"].append(today)
            save_data(data)
            print(f"Habit '{habit_name}' marked complete for today.")

def generate_weekly_report():
    data = load_data()
    today = datetime.today()
    week_ago = today - timedelta(days=6)  # Include today + 6 past days

    if not data:
        print("No habits to report.")
        return

    print("\nWeekly Habit Report (Last 7 Days):")
    print("==================================")

    for habit, info in data.items():
        dates = info.get("dates_completed", [])
        recent_dates = [
            date for date in dates
            if datetime.strptime(date, "%Y-%m-%d") >= week_ago
        ]
        print(f"\nHabit: {habit}")
        print(f"Completions: {len(recent_dates)} / 7 days")
        if recent_dates:
            print("Dates: " + ", ".join(recent_dates))
        else:
            print("No completions this week.")

def delete_habit(habit_name):
    data = load_data()
    if habit_name not in data:
        print(f"Habit '{habit_name}' does not exist.")
    else:
        del data[habit_name]
        save_data(data)
        print(f"Habit '{habit_name}' has been deleted.")

def list_habits():
    data = load_data()
    if not data:
        print("You are not tracking any habits yet.")
        return

    print("\nTracked Habits:")
    print("================")
    for idx, habit in enumerate(data.keys(), start=1):
        print(f"{idx}. {habit}")


