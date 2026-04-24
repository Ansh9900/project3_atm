import utils

def deposit():
    a = int(input("enter the amount: "))
    utils.transactions.append(f"Deposited: {a}")
    utils.balance = utils.balance + a
    print(f"Success! Deposited {a}")


