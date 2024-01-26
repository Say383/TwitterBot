class PortfolioTracker:
    def __init__(self):
        self.holdings = {'bitcoin': 0.5, 'ethereum': 2, 'litecoin': 10}
        self.purchase_prices = {'bitcoin': 40000, 'ethereum': 2000, 'litecoin': 150}

    def update_prices(self):
        for coin_id in self.holdings.keys():
            current_price = get_current_price(coin_id)
            self.holdings[coin_id] = (self.holdings[coin_id], current_price)

    def calculate_portfolio_value(self):
        total_value = 0
        for amount, price in self.holdings.values():
            total_value += amount * price
        return total_value

    def calculate_gains_losses(self):
        gains_losses = {}
        for coin_id, (amount, current_price) in self.holdings.items():
            purchase_price = self.purchase_prices[coin_id]
            gains_losses[coin_id] = (current_price - purchase_price) * amount
        return gains_losses

class Asset:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Stock(Asset):
    def __init__(self, name, value, ticker_symbol):
        super().__init__(name, value)
        self.ticker_symbol = ticker_symbol

class Bond(Asset):
    def __init__(self, name, value, interest_rate):
        super().__init__(name, value)
        self.interest_rate = interest_rate

# Usage
my_stock = Stock("TechCorp", 1500, "TC")
my_bond = Bond("GovBond", 1000, 0.05)

# Usage
portfolio = PortfolioTracker()
portfolio.update_prices()
print(f"Total Portfolio Value: ${portfolio.calculate_portfolio_value()}")
print("Gains/Losses per Asset:", portfolio.calculate_gains_losses())
