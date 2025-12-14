import tkinter as tk
from tkinter import messagebox
from password_utils import strength_level, suggestions, generate_password

# ---------- Window ----------
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("550x450")
root.configure(bg="#0f0f0f")
root.resizable(False, False)

# ---------- Functions ----------
def analyze_password():
    pwd = password_entry.get()
    if not pwd:
        messagebox.showwarning("Warning", "Enter a password first!")
        return

    level = strength_level(pwd)

    colors = {
        "Weak": "#ff4d4d",
        "Medium": "#ffa500",
        "Strong": "#00ff99",
        "Very Strong": "#00ccff"
    }

    result_label.config(
        text=f"Strength: {level}",
        fg=colors.get(level, "white")
    )

    tips = suggestions(pwd)
    if tips:
        tips_text = "\n• " + "\n• ".join(tips)
    else:
        tips_text = "\n• Excellent password!"

    suggestions_label.config(text=tips_text)

def generate_and_analyze():
    pwd = generate_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, pwd)
    analyze_password()

# ---------- Title ----------
title_label = tk.Label(
    root,
    text="Password Strength Analyzer",
    font=("Consolas", 20, "bold"),
    bg="#0f0f0f",
    fg="#00ffcc"
)
title_label.pack(pady=15)

# ---------- Password Entry ----------
password_entry = tk.Entry(
    root,
    width=32,
    font=("Consolas", 14),
    bg="#1e1e1e",
    fg="white",
    insertbackground="white",
    relief="flat"
)
password_entry.pack(pady=10)

# ---------- Buttons ----------
btn_frame = tk.Frame(root, bg="#0f0f0f")
btn_frame.pack(pady=10)

analyze_button = tk.Button(
    btn_frame,
    text="Analyze",
    font=("Consolas", 12, "bold"),
    bg="#222222",
    fg="#00ffcc",
    activebackground="#00ffcc",
    activeforeground="black",
    width=14,
    command=analyze_password
)
analyze_button.grid(row=0, column=0, padx=10)

generate_button = tk.Button(
    btn_frame,
    text="Generate Strong",
    font=("Consolas", 12, "bold"),
    bg="#222222",
    fg="#00ffcc",
    activebackground="#00ffcc",
    activeforeground="black",
    width=14,
    command=generate_and_analyze
)
generate_button.grid(row=0, column=1, padx=10)

# ---------- Result ----------
result_label = tk.Label(
    root,
    text="",
    font=("Consolas", 16, "bold"),
    bg="#0f0f0f"
)
result_label.pack(pady=15)

# ---------- Suggestions ----------
suggestions_label = tk.Label(
    root,
    text="",
    font=("Consolas", 12),
    bg="#0f0f0f",
    fg="white",
    justify="left",
    wraplength=500
)
suggestions_label.pack(pady=10)

# ---------- Footer ----------
footer_label = tk.Label(
    root,
    text="created by SIMOEEEEX",
    font=("Consolas", 10),
    bg="#0f0f0f",
    fg="#666666"
)
footer_label.pack(side="bottom", pady=10)

# ---------- Run ----------
root.mainloop()

