from portfolio import Transaction, Portfolio, Currency, Money, Direction

if __name__ == '__main__':
    print('Hi');
    print(Currency(Currency.EUR))

    tr = Transaction(1588113697, 'FB', 14, Money(220, 50, Currency.USD), Direction.BUY)
    print(tr)
