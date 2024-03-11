import numpy as np
stocks_price = {
    'info'  : [600,630,620],
    'ril'   : [1430,1490,1567],
    'mtl'   : [234,180,160]
}

def print_all():
    for stock in stocks_price:
        avg = round(np.average(stocks_price[stock]), 2)
        print(stock + " ==> " + str(stocks_price[stock]) + " ==> " + "avg: "+ str(avg))
def add():
    print("Please enter the stock ticker: ")
    new_stock = str(input())
    print("Please enter the price: ")
    new_price = int(input())
    if new_stock in stocks_price:
        stocks_price[new_stock].append(new_price)
        print_all()
    else:
        stocks_price.update({new_stock: [new_price]})
        print_all()

def main():
    print("Enter the command you want to perform (print or add): ")
    command = str(input())

    if command == "print":
        print_all()
    elif command == "add":
        add()


if __name__ == '__main__':
    main()