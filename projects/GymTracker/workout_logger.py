import pandas as pd
from datetime import datetime
import os

WORKOUT_FILE = "data/workouts.csv"

def init_workouts():
    if not os.path.exists(WORKOUT_FILE):
        df = pd.DataFrame(columns=["date_time", "exercise", "sets", "reps", "weight"])
        df.to_csv(WORKOUT_FILE, index=False)

def log_workout(exercise, sets, reps, weight):
    init_workouts()
    df = pd.read_csv(WORKOUT_FILE)
    df.loc[len(df)] = [
        datetime.now().strftime("%Y-%m-%d %H:%M"),
        exercise,
        sets,
        reps,
        weight
    ]
    df.to_csv(WORKOUT_FILE, index=False)

def load_workouts():
    init_workouts()
    return pd.read_csv(WORKOUT_FILE)

