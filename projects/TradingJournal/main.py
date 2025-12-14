import tkinter as tk
from tkinter import ttk, messagebox
from trade_logger import init_journal, log_trade
from analyzer import load_trades, equity_curve, win_rate, risk_reward, max_drawdown
from charts import plot_equity, plot_profit_distribution

init_journal()

# ====== Functions ======
def submit_trade():
    try:
        symbol = symbol_entry.get()
        side = side_var.get()
        lot = float(lot_entry.get())
        strategy = strategy_entry.get()
        bias = bias_var.get()
        risked = float(risk_entry.get())
        rrr = float(rrr_entry.get())

        # For simplicity, we store RRR as additional info in 'profit' calculation
        # In actual backtest, profit is calculated from entry/exit price
        profit = round(risked * rrr if side.upper() == "BUY" else -risked * rrr, 2)

        # Log trade
        log_trade(symbol, side, 0, 0, lot, strategy, bias, risked)
        messagebox.showinfo("Success", f"✅ Trade logged successfully!\nProfit estimate: ${profit}")
        clear_entries()
        update_table()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_entries():
    symbol_entry.delete(0, tk.END)
    lot_entry.delete(0, tk.END)
    strategy_entry.delete(0, tk.END)
    risk_entry.delete(0, tk.END)
    rrr_entry.delete(0, tk.END)

def show_summary():
    df = load_trades()
    if df.empty:
        messagebox.showinfo("Summary", "No trades yet.")
        return

    equity = equity_curve(df)
    summary_text = f"""
Total Trades: {len(df)}
Win Rate: {win_rate(df)}%
Net Profit: ${df['profit'].sum():.2f}
Risk/Reward: {risk_reward(df)}
Max Drawdown: ${max_drawdown(equity)}
"""
    messagebox.showinfo("Trading Summary", summary_text)

def show_equity_curve():
    plot_equity()

def show_profit_dist():
    plot_profit_distribution()

def update_table():
    for row in trade_table.get_children():
        trade_table.delete(row)
    df = load_trades()
    for i, row in df.iterrows():
        trade_table.insert("", "end", values=(
            row["date_time"],
            row["symbol"],
            row["side"],
            row["lot"] if "lot" in row else row["qty"],
            row["strategy"],
            row["bias"],
            row["risked"],
            row["profit"]
        ))

# ====== GUI ======
root = tk.Tk()
root.title("Trading Journal by SIMOEEEEX")
root.configure(bg="#121212")
root.geometry("900x500")

# ==== Input Frame ====
input_frame = tk.Frame(root, bg="#1f1f1f", padx=10, pady=10)
input_frame.pack(side="top", fill="x", padx=10, pady=10)

# Input fields
symbol_entry = tk.Entry(input_frame, width=12)
lot_entry = tk.Entry(input_frame, width=10)
strategy_entry = tk.Entry(input_frame, width=12)
risk_entry = tk.Entry(input_frame, width=10)
rrr_entry = tk.Entry(input_frame, width=10)

side_var = tk.StringVar(value="BUY")
side_menu = ttk.Combobox(input_frame, textvariable=side_var, values=["BUY", "SELL"], width=8)

bias_var = tk.StringVar(value="Bullish")
bias_menu = ttk.Combobox(input_frame, textvariable=bias_var, values=["Bullish", "Bearish", "Neutral"], width=8)

# Place inputs in grid
tk.Label(input_frame, text="Symbol:", fg="white", bg="#1f1f1f").grid(row=0, column=0, padx=5, pady=5)
symbol_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Side:", fg="white", bg="#1f1f1f").grid(row=0, column=2, padx=5, pady=5)
side_menu.grid(row=0, column=3, padx=5, pady=5)

tk.Label(input_frame, text="Lot:", fg="white", bg="#1f1f1f").grid(row=0, column=4, padx=5, pady=5)
lot_entry.grid(row=0, column=5, padx=5, pady=5)

tk.Label(input_frame, text="Strategy:", fg="white", bg="#1f1f1f").grid(row=1, column=0, padx=5, pady=5)
strategy_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Bias:", fg="white", bg="#1f1f1f").grid(row=1, column=2, padx=5, pady=5)
bias_menu.grid(row=1, column=3, padx=5, pady=5)

tk.Label(input_frame, text="Risked ($):", fg="white", bg="#1f1f1f").grid(row=1, column=4, padx=5, pady=5)
risk_entry.grid(row=1, column=5, padx=5, pady=5)

tk.Label(input_frame, text="RRR:", fg="white", bg="#1f1f1f").grid(row=2, column=0, padx=5, pady=5)
rrr_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
tk.Button(input_frame, text="Log Trade", command=submit_trade, bg="#4caf50", fg="white", width=15).grid(row=2, column=2, padx=5, pady=10)
tk.Button(input_frame, text="Show Summary", command=show_summary, bg="#2196f3", fg="white", width=15).grid(row=2, column=3, padx=5, pady=10)
tk.Button(input_frame, text="Equity Curve", command=show_equity_curve, bg="#ff9800", fg="white", width=15).grid(row=2, column=4, padx=5, pady=10)
tk.Button(input_frame, text="Profit Dist.", command=show_profit_dist, bg="#9c27b0", fg="white", width=15).grid(row=2, column=5, padx=5, pady=10)

# ==== Trade Table ====
table_frame = tk.Frame(root, bg="#121212")
table_frame.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("date_time", "symbol", "side", "lot", "strategy", "bias", "risked", "profit")
trade_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
for col in columns:
    trade_table.heading(col, text=col)
    trade_table.column(col, width=100 if col!="strategy" else 120)
trade_table.pack(fill="both", expand=True)

# Style
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#1f1f1f", foreground="white", fieldbackground="#1f1f1f")
style.configure("Treeview.Heading", background="#333333", foreground="white", font=("Arial", 10, "bold"))

update_table()

# Footer
footer = tk.Label(root, text="Created by SIMOEEEEX", bg="#121212", fg="#888888", font=("Arial", 10))
footer.pack(side="bottom", pady=5)

root.mainloop()

