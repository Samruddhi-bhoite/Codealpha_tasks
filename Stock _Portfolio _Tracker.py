def stock_tracker():
    stock_prices = {
        "AAPL": 188,
        "TSLA": 250,
        "GOOG": 150,
        "AMZN": 200
    }

    total_investment = 0

    print("Stock Portfolio Tracker")
    print("Available stocks:", stock_prices)
    print("Type 'done' to finish\n")

    while True:
        stock = input("Enter stock name: ").upper()

        if stock == "DONE":
            break

        if stock in stock_prices:
            quantity = int(input("Enter quantity: "))
            investment = stock_prices[stock] * quantity
            total_investment += investment

            print(f"Added {stock} → ₹{investment}\n")
        else:
            print("Stock not found!\n")

    print("Total Investment Value: ₹", total_investment)

stock_tracker()
