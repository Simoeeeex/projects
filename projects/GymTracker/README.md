# Gym Tracker

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

**Created by SIMOEEEEX**

---

## Description

**Gym Tracker** is a professional app to track workouts and body measurements.

It helps users:
- Log exercises with sets, reps, and weights
- Record body measurements (weight, body fat, chest, arms, legs, waist)
- View stats like total workout volume, best exercise, and weight change
- Visualize progress with charts
- Plan workouts based on goals (strength, hypertrophy, cutting)

---

## Features

- ✅ Log workouts and body measurements
- ✅ View statistics: total volume, best exercise, weight change
- ✅ Track progress over time with graphs
- ✅ Generate basic workout plans
- ✅ Professional black-themed GUI
- ✅ Footer: "Created by SIMOEEEEX"

---

## Data

All data is stored in the **data/** folder:

- `workouts.csv` → workout logs
- `measurements.csv` → body measurements

---

## Installation

1. Make sure **Python 3** is installed  
2. Go to the project folder:

```bash
cd GymTracker
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the app:

bash
Copy code
python3 main.py
Usage
Open the app

Log your workouts and measurements

Click Show Stats to view performance

Use charts to track progress visually

Project Structure
graphql
Copy code
GymTracker/
│
├── main.py                    # Launch GUI
├── workout_logger.py          # Log and load workouts
├── measurement_logger.py      # Log and load measurements
├── analyzer.py                # Calculate stats
├── charts.py                  # Plot graphs
├── planner.py                 # Generate workout plans
├── data/
│   ├── workouts.csv
│   └── measurements.csv
├── tests/
│   ├── test_workout_logger.py
│   ├── test_measurement_logger.py
│   └── test_analyzer.py
├── requirements.txt
└── README.md
License
Free to use for learning and personal tracking.

Created by SIMOEEEEX
