def generate_plan(goal="hypertrophy"):
    if goal == "strength":
        return {
            "Day 1": ["Squat 5x5", "Bench Press 5x5"],
            "Day 2": ["Deadlift 5x5", "Pull Ups 4x8"]
        }
    if goal == "cut":
        return {
            "Day 1": ["Circuit Training", "HIIT"],
            "Day 2": ["Full Body Light Weights"]
        }
    return {
        "Day 1": ["Chest + Triceps"],
        "Day 2": ["Back + Biceps"],
        "Day 3": ["Legs"],
        "Day 4": ["Shoulders + Abs"]
    }

