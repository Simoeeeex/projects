import tkinter as tk
from tkinter import ttk, messagebox
from workout_logger import log_workout, load_workouts
from measurement_logger import log_measurement, load_measurements
from analyzer import total_volume, best_exercise, weight_change
from charts import plot_weight, plot_volume

root = tk.Tk()
root.title("Gym Tracker by SIMOEEEEX")
root.geometry("900x600")
root.configure(bg="#121212")

# ================= WORKOUT =================
frame_w = tk.LabelFrame(root, text="Workout Logger", bg="#1f1f1f", fg="white")
frame_w.pack(fill="x", padx=10, pady=10)

entries = {}
labels = ["Exercise", "Sets", "Reps", "Weight"]
for i, lbl in enumerate(labels):
    tk.Label(frame_w, text=lbl, bg="#1f1f1f", fg="white").grid(row=0, column=i*2)
    e = tk.Entry(frame_w)
    e.grid(row=0, column=i*2+1)
    entries[lbl] = e

def save_workout():
    log_workout(
        entries["Exercise"].get(),
        int(entries["Sets"].get()),
        int(entries["Reps"].get()),
        float(entries["Weight"].get())
    )
    messagebox.showinfo("Saved", "Workout logged")

tk.Button(frame_w, text="Save", command=save_workout).grid(row=0, column=8, padx=10)

# ================= MEASUREMENTS =================
frame_m = tk.LabelFrame(root, text="Body Measurements", bg="#1f1f1f", fg="white")
frame_m.pack(fill="x", padx=10, pady=10)

me = {}
m_labels = ["Weight", "Body Fat", "Chest", "Arms", "Legs", "Waist"]
for i, lbl in enumerate(m_labels):
    tk.Label(frame_m, text=lbl, bg="#1f1f1f", fg="white").grid(row=0, column=i*2)
    e = tk.Entry(frame_m)
    e.grid(row=0, column=i*2+1)
    me[lbl] = e

def save_measurement():
    log_measurement(
        float(me["Weight"].get()),
        float(me["Body Fat"].get()),
        float(me["Chest"].get()),
        float(me["Arms"].get()),
        float(me["Legs"].get()),
        float(me["Waist"].get())
    )
    messagebox.showinfo("Saved", "Measurement logged")

tk.Button(frame_m, text="Save", command=save_measurement).grid(row=0, column=12, padx=10)

# ================= STATS =================
frame_s = tk.LabelFrame(root, text="Stats & Analysis", bg="#1f1f1f", fg="white")
frame_s.pack(fill="x", padx=10, pady=10)

def show_stats():
    w = load_workouts()
    m = load_measurements()
    stats = f"""
Total Volume: {total_volume(w)}
Best Exercise: {best_exercise(w)}
Weight Change: {weight_change(m)}
"""
    messagebox.showinfo("Stats", stats)

tk.Button(frame_s, text="Show Stats", command=show_stats).pack(side="left", padx=5)
tk.Button(frame_s, text="Weight Chart", command=lambda: plot_weight(load_measurements())).pack(side="left", padx=5)
tk.Button(frame_s, text="Volume Chart", command=lambda: plot_volume(load_workouts())).pack(side="left", padx=5)

# ================= FOOTER =================
tk.Label(root, text="Created by SIMOEEEEX", bg="#121212", fg="#888888").pack(side="bottom", pady=10)

root.mainloop()

