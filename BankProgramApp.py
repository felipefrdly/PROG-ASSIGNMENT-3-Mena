from BankProgram import Application
from BankProgram import Bank
from BankProgram import *

if __name__ == "__main__":
    App = Application()
    BoC = Bank()

    #Test cases for anyone marking :) these are pre defined accounts for you to access and not required for the program to run
    acc1 = SavingsAccount(1111, "Felipe", 0.5, 10000, 5000)  #minimum balance is 5000
    acc2 = SavingsAccount(2222, "Joe", 0.5, 5000, 2000) #minimum balance is 2000
    acc3 = SavingsAccount(3333, "Robert", 0.5, 1000, 500)  #minimum balance is 500
    acc4 = ChequingAccount(4444, "Jerry", 0.5, 5000, 5000) #overdraft is 5000
    acc5 = ChequingAccount(5555, "Laura", 0.5, 7000, 1000) #overdraft is 1000
    acc6 = ChequingAccount(6666, "Sarah", 0.5, 30, 20) #overdraft is 20

    App.run(BoC)
