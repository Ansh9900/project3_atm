import utils
def statement():    
    if not utils.transactions:
        print("No transactions yet.")
    else:
        for i in utils.transactions:
            print(i)    