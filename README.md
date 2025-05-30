# Habit Tracker (CLI-based)

A lightweight, command-line habit tracking tool written in Python. This app helps users add, track, and report daily habits with a clean interface and persistent storage using JSON files.

---

## Features

- Add and store multiple daily habits
- Mark habits as completed for today
- View a weekly completion report
- List all tracked habits
- Delete habits you no longer need
- Local persistent storage in `JSON`
- Unit tested with `unittest` and `mock`

---

## Folder Structure

```
habit-tracker/
│
├── main.py                      # CLI Entry point
├── habit_manager.py             # Core logic for habit management
├── data/
│   └── habits_data.json         # JSON file for persistent habit data
├── tests/
│   └── test_habit_manager.py    # Unit tests using unittest and mock
├── docs/
│   ├── wireframe.png
│   ├── architecture.png
└── README.md
```

---

## Setup Instructions

### Requirements

- Python 3.7+
- No external libraries needed (uses built-in `json`, `datetime`, `unittest`, and `mock`)

### Installation

1. Clone or download the repository:
   ```bash
   git clone https://github.com/bmdesai0309/Habit_tracker.git
   cd Habit_tracker
   ```

2. Ensure the following file exists (create it manually if needed):
   ```bash
   touch data/habits_data.json
   ```

3. Add this content to the file:
   ```json
   {}
   ```

---

## Running the Application

From the project root, run:

```bash
python main.py
```

You will see a CLI menu like:

```
Simple Habit Tracker
====================
1. Add a new habit
2. Mark habit as completed
3. View weekly report
4. Delete a habit
5. List all habits
6. Exit
```

Follow the prompts to interact with your habits.

---

## Running Tests

To run all unit tests:

```bash
python -m unittest discover -s tests
```

You’ll see test output confirming if all features are functioning correctly.

---

## Author

**Balmukund Desai**  
CU Software Engineering Residency Project  
May 2025
