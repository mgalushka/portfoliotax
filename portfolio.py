from transaction import Transaction, Money

class Portfolio:
    def __init__(self):
        self.transactions = []

    def add_transactions(self, transactions: [Transaction]) -> None:
        self.transactions.extend(transactions)

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)

    def __repr__(self) -> str:
        result: str = ""
        for tr in self.transactions:
            result += str(tr)
            result += '\n'
        return result
