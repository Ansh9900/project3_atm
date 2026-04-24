from deposit import deposit
from display import display
from withdraw import withdraw
from statement import statement
def atm():
        while True:
            print("""
        1 - Display Balance
        2 - Withdraw Money
        3 - Deposit Money
        4 - Statement
        5 - exit""")
            choice = input("enter your choice")
            if(choice == "1"): display()
            elif(choice == "2"): withdraw()
            elif(choice == "3"): deposit()
            elif(choice == "4"): statement()
            elif(choice == "5"):
                break
            else: 
                print("invalid input")

atm()