from portfolio import Transaction, Portfolio, Currency, Money, Direction

if __name__ == '__main__':
    print(Currency.EUR.name)

    tr = Transaction(1588113697, 'FB', 14, Money(220.5, Currency.USD), Direction.BUY)
    print(tr)
