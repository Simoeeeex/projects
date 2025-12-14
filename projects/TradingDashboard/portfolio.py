class Portfolio:
    def __init__(self, initial_balance=10000):
        self.balance = initial_balance
        self.position = 0      # How much crypto/forex we hold
        self.avg_price = 0     # Average buy price
        self.trade_history = []  # List of executed trades

    def execute_signal(self, signal, price, symbol="BTC"):
        """
        Execute BUY/SELL signals at given price
        """
        if signal == "BUY" and self.balance > 0:
            # Buy as much as possible
            qty = self.balance / price
            self.position += qty
            self.avg_price = price
            self.balance = 0
            self.trade_history.append({"type": "BUY", "price": price, "qty": qty, "symbol": symbol})
            print(f"BUY {qty:.6f} {symbol} at ${price:.2f}")

        elif signal == "SELL" and self.position > 0:
            # Sell all position
            self.balance += self.position * price
            self.trade_history.append({"type": "SELL", "price": price, "qty": self.position, "symbol": symbol})
            print(f"SELL {self.position:.6f} {symbol} at ${price:.2f}")
            self.position = 0

    def current_value(self, current_price):
        """
        Return current portfolio value
        """
        return self.balance + self.position * current_price

    def print_summary(self, current_price):
        print("=== Portfolio Summary ===")
        print(f"Balance: ${self.balance:.2f}")
        print(f"Position: {self.position:.6f}")
        print(f"Portfolio Value: ${self.current_value(current_price):.2f}")
        print(f"Trade History: {self.trade_history}")

