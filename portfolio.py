from enum import Enum
from datetime import datetime


class Currency(Enum):
    EUR = 'EUR'
    USD = 'USD'
    GBP = 'GBP'

class Money:
    def __init__(self, whole: int, fraction: int, currency: Currency) -> None:
        self.whole = whole
        self.fraction = fraction
        self.currency = currency

    def __repr__(self) -> str:
        return "{}.{} {}".format(self.whole, self.fraction, self.currency.name)

    @staticmethod
    def parse_from_string(input: str) -> None:
        return None


class Direction(Enum):
    BUY = 'BUY'
    SELL = 'SELL'

class Transaction:
    def __init__(
        self,
        date: int,              # unixtime for transaction date
        index: str,             # index
        amount: int,            # amount
        price: Money,           # transaction amount
        direction: Direction    # buy/sell
    ) -> None:
        self.date = date
        self.index = index
        self.amount = amount
        self.price = price
        self.direction = direction

    def __repr__(self) -> str:
        return "[{dt}] {direction} {amount} {index} @ {price}".format(
            dt=datetime.utcfromtimestamp(self.date).strftime('%Y-%m-%d'),
            direction=self.direction.name,
            amount=self.amount,
            index=self.index,
            price=self.price,
        )

class Portfolio:
    def __init__(self):
        pass

    def add_transactions(transaction: Transaction) -> None:
        pass
