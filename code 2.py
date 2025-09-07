# Stock Portfolio Tracker

# Hardcoded stock prices (in USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 3400,
    "MSFT": 310
}

def stock_tracker():
    portfolio = {}   # store user stocks
    total_value = 0

    print("📈 Welcome to Stock Portfolio Tracker")
    print("Available stocks and their prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("❌ Stock not found. Please choose from the list.")
            continue

        try:
            qty = int(input(f"Enter quantity of {stock}: "))
            if qty <= 0:
                print("⚠️ Quantity must be positive.")
                continue
        except ValueError:
            print("❌ Invalid input. Enter a number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + qty

    print("\n📊 Your Portfolio Summary:")
    for stock, qty in portfolio.items():
        value = qty * stock_prices[stock]
        total_value += value
        print(f"{stock} - {qty} shares → ${value}")

    print(f"\n💰 Total Investment Value: ${total_value}")

    # Optionally save results to file
    save = input("Do you want to save results to a file? (yes/no): ").lower()
    if save == "yes":
        with open("portfolio.txt", "w") as file:
            file.write("📊 Portfolio Summary:\n")
            for stock, qty in portfolio.items():
                value = qty * stock_prices[stock]
                file.write(f"{stock} - {qty} shares → ${value}\n")
            file.write(f"\n💰 Total Investment Value: ${total_value}\n")
        print("✅ Portfolio saved to portfolio.txt")

# Run the tracker
stock_tracker()
