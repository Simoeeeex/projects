import matplotlib.pyplot as plt
import pandas as pd

def plot_weight(df):
    if df.empty:
        return
    plt.figure(figsize=(8,4))
    plt.plot(pd.to_datetime(df["date_time"]), df["weight"], marker="o")
    plt.title("Weight Progress")
    plt.xlabel("Date")
    plt.ylabel("Weight")
    plt.grid(True)
    plt.show()

def plot_volume(workouts_df):
    if workouts_df.empty:
        return
    workouts_df["volume"] = workouts_df["sets"] * workouts_df["reps"] * workouts_df["weight"]
    plt.figure(figsize=(8,4))
    plt.plot(pd.to_datetime(workouts_df["date_time"]), workouts_df["volume"], marker="o")
    plt.title("Workout Volume Progress")
    plt.xlabel("Date")
    plt.ylabel("Volume")
    plt.grid(True)
    plt.show()

