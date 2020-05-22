class Currency:
    EUR = 'EUR'
    USD = 'USD'
    EUR = 'EUR'

    def __init__(self, currency: str) -> None:
        self.currency = currency

    def __repr__(self) -> str:
        return self.currency


class Money:
    def __init__(self, whole: int, fraction: int, currency: Currency) -> None:
        self.whole = whole
        self.fraction = fraction
        self.currency = currency

    def __repr__(self) -> str:
        return "{}.{} {}".format(self.whole, self.fraction, self.currency)

    @staticmethod
    def parse_from_string(input: str) -> None:
        return None


class Transaction:
    date: int # unixtime for transaction date
    index: str # index
    price: Money # transaction amount

    def __init__(self):
        pass


class Portfolio:
    def __init__(self):
        pass

    def add_transactions(transaction: Transaction) -> None:
        pass
