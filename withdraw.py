import utils 

def withdraw():
    amt = int(input("amount you want to withdraw: "))
    if utils.balance < amt:
        print("insufficient balance")
    else:
        utils.transactions.append(f"Withdrawn: ${amt}")
        utils.balance = utils.balance - amt
        print(f"Success! Remaining balance: ${utils.balance}")    
