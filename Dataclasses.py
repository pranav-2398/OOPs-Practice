from dataclasses import dataclass
from functools import total_ordering


@dataclass(frozen=True)
class Stock:
    ticker: str
    price: int
    dividend: float = 0
    dividend_frequency: int = 4

    @property
    def annual_dividend(self):
        return self.dividend * self.dividend_frequency


@total_ordering
@dataclass
class Position:
    stock: Stock
    shares: int

    def __eq__(self, other):
        if isinstance(other, Position):
            if self.stock.price == other.stock.price:
                return self.shares == other.shares

            else:
                return False

    def __gt__(self, other):
        if isinstance(other, Position):
            return self.shares > other.shares

        else:
            return False


@dataclass
class Portfolio:
    holdings: [Position]

    @property
    def value(self):
        return sum(a.stock.price * a.shares for a in self.holdings)

    @property
    def portfolio_yield(self):
        return sum([a.stock.annual_dividend * a.shares for a in self.holdings]) / self.value


MSFT = Stock("MSFT", 360, 0.62, 4)
LMT = Stock("LMT", 360, 2.80, 4)
GOOGL = Stock("GOOGL", 2200, 0, 0)

# print(LMT)
# LMT.dividend = 3.2
# print(LMT.annual_dividend)

p1 = Position(MSFT, 100)
p2 = Position(LMT, 100)
p3 = Position(GOOGL, 10)

portfolio = Portfolio(holdings=[p1, p2, p3])

# print(portfolio)
print(portfolio.value)
print(f"{portfolio.portfolio_yield:.2%}")
