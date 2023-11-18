from BankProgram import Application
from BankProgram import Bank
from BankProgram import *

if __name__ == "__main__":
    App = Application()
    BoC = Bank()

    #Test cases for anyone marking :) these are pre defined accounts for you to access and not required for the program to run
    acc1 = Account(1111, "Felipe", 0.5, 5000)
    acc2 = SavingsAccount(2222, "Joe", 0.5, 5000, 2000) #minimum balance is 2000
    acc3 = ChequingAccount(3333, "Jerry", 0.5, 5000, 5000) #overdraft is 5000

    App.run(BoC)
