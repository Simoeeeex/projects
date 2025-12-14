def total_volume(workouts_df):
    if workouts_df.empty:
        return 0
    return (workouts_df["sets"] * workouts_df["reps"] * workouts_df["weight"]).sum()

def best_exercise(workouts_df):
    if workouts_df.empty:
        return None
    workouts_df["volume"] = workouts_df["sets"] * workouts_df["reps"] * workouts_df["weight"]
    return workouts_df.groupby("exercise")["volume"].sum().idxmax()

def weight_change(measurements_df):
    if len(measurements_df) < 2:
        return 0
    return measurements_df.iloc[-1]["weight"] - measurements_df.iloc[0]["weight"]

