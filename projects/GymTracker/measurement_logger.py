import pandas as pd
from datetime import datetime
import os

MEASUREMENT_FILE = "data/measurements.csv"

def init_measurements():
    if not os.path.exists(MEASUREMENT_FILE):
        df = pd.DataFrame(columns=[
            "date_time", "weight", "body_fat", "chest", "arms", "legs", "waist"
        ])
        df.to_csv(MEASUREMENT_FILE, index=False)

def log_measurement(weight, body_fat, chest, arms, legs, waist):
    init_measurements()
    df = pd.read_csv(MEASUREMENT_FILE)
    df.loc[len(df)] = [
        datetime.now().strftime("%Y-%m-%d %H:%M"),
        weight, body_fat, chest, arms, legs, waist
    ]
    df.to_csv(MEASUREMENT_FILE, index=False)

def load_measurements():
    init_measurements()
    return pd.read_csv(MEASUREMENT_FILE)

