import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from data_fetch import fetch_data
from indicators import add_ema_rsi
from strategy import generate_signals
from portfolio import Portfolio

# Symbols list
SYMBOLS = ["BTC-USD", "ETH-USD", "EURUSD=X", "GBPUSD=X"]

# Create portfolio
port = Portfolio(10000)

# ---------- Functions ----------
def update_dashboard():
    symbol = symbol_var.get()
    if not symbol:
        messagebox.showwarning("Warning", "Select a symbol!")
        return

    # Fetch and process data
    df = fetch_data(symbol)
    if df is None or df.empty:
        messagebox.showerror("Error", "Failed to fetch data!")
        return

    df = add_ema_rsi(df)
    df = generate_signals(df)

    # Simulate trades for last candle
    last_row = df.iloc[-1]
    port.execute_signal(last_row["signal"], last_row["close"])

    # Clear previous figures
    for widget in chart_frame.winfo_children():
        widget.destroy()

    # Create figure
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,6), gridspec_kw={'height_ratios':[3,1]})
    fig.patch.set_facecolor('#0f0f0f')
    ax1.set_facecolor('#0f0f0f')
    ax2.set_facecolor('#0f0f0f')

    # Plot Close and EMAs
    ax1.plot(df["time"], df["close"], label="Close", color="#00ffcc")
    ax1.plot(df["time"], df["ema_50"], label="EMA50", color="#ff9900")
    ax1.plot(df["time"], df["ema_200"], label="EMA200", color="#ff4d4d")
    ax1.legend(facecolor="#1e1e1e", labelcolor="white")
    ax1.set_title(f"{symbol} Price & EMAs", color="white")

    # Plot RSI
    ax2.plot(df["time"], df["rsi"], label="RSI", color="#00ccff")
    ax2.axhline(70, color="red", linestyle="--")
    ax2.axhline(30, color="green", linestyle="--")
    ax2.set_title("RSI", color="white")
    ax2.legend(facecolor="#1e1e1e", labelcolor="white")

    # Draw canvas
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Update info labels
    last_signal_var.set(f"Last Signal: {last_row['signal']}")
    balance_var.set(f"Balance: ${port.balance:.2f}")
    position_var.set(f"Position: {port.position:.6f}")
    total_var.set(f"Portfolio Value: ${port.current_value(last_row['close']):.2f}")

# ---------- GUI ----------
root = tk.Tk()
root.title("Trading Dashboard")
root.geometry("900x700")
root.configure(bg="#0f0f0f")
root.resizable(False, False)

# Symbol selection
symbol_var = tk.StringVar()
symbol_label = tk.Label(root, text="Select Symbol:", bg="#0f0f0f", fg="white", font=("Consolas", 12))
symbol_label.pack(pady=5)
symbol_menu = ttk.Combobox(root, textvariable=symbol_var, values=SYMBOLS, font=("Consolas", 12))
symbol_menu.pack(pady=5)
symbol_menu.current(0)

# Update button
update_button = tk.Button(root, text="Refresh & Run Strategy", bg="#222222", fg="#00ffcc",
                          font=("Consolas", 12, "bold"), command=update_dashboard)
update_button.pack(pady=5)

# Info labels
last_signal_var = tk.StringVar()
balance_var = tk.StringVar()
position_var = tk.StringVar()
total_var = tk.StringVar()

info_frame = tk.Frame(root, bg="#0f0f0f")
info_frame.pack(pady=5)
tk.Label(info_frame, textvariable=last_signal_var, bg="#0f0f0f", fg="white", font=("Consolas", 12)).pack()
tk.Label(info_frame, textvariable=balance_var, bg="#0f0f0f", fg="white", font=("Consolas", 12)).pack()
tk.Label(info_frame, textvariable=position_var, bg="#0f0f0f", fg="white", font=("Consolas", 12)).pack()
tk.Label(info_frame, textvariable=total_var, bg="#0f0f0f", fg="white", font=("Consolas", 12)).pack()

# Chart frame
chart_frame = tk.Frame(root, bg="#0f0f0f")
chart_frame.pack(pady=10)

# Footer
footer = tk.Label(root, text="created by SIMOEEEEX", bg="#0f0f0f", fg="#666666", font=("Consolas", 10))
footer.pack(side="bottom", pady=10)

root.mainloop()

