from transaction import Transaction, Currency, Money, Direction
from portfolio import Portfolio

if __name__ == '__main__':
    print(Currency.EUR.name)

    tr = Transaction(1588113697, 'FB', 14, Money(220.5, Currency.USD), Direction.BUY)
    print(tr)

    p = Portfolio()
    p.add_transaction(tr)
    print(p)
