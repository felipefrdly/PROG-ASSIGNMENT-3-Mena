"""
Author: Felipe Mena
Date: 05/11/2023
Description:
"""

class Application:
    def run(self):
        self.showMainMenu()#creates an instance of main menu when called

    def showMainMenu(self):
        print("___Welcome to Bank of Canada___\n\n<1> Select Account\n<2> Open Account\n<3> Exit\n") #displays options

        #This loop keeps the user inside of it until they input one of the available options 
        while True:
            choice = input("Please select one of the available options: ") #takes user input

            #asks for account number and calls showAccountMenu method if 1 is chosen
            if choice == "1":
                print("Option 1 Selected")
                accountSelect = input("Enter account number: ")
                self.showAccountMenu()
                break
            
            elif choice == "2":
                print("Option 2 Selected")
                break

            #exits the program if 3 is chosen            
            elif choice == "3":
                print("Exiting Bank of Canada, Have a good day!")
                exit()
                break

            else:
                print("Please try again.")
                continue

    def showAccountMenu(self):
        print("\n___Account Menu___\n\n<1> Check Balance\n<2> Deposit\n<3> Withdraw\n<4> Exit Account\n")

        #This loop keeps the user inside of it until they input one of the available options 
        while True:
            choice = input("Please select one of the available options: ")#takes user input

            #these 5 statements check if one of the options are selected, execute diffrent methods based on option
            if choice == "1":
                print("Option 1 Selected")
                break
            
            elif choice == "2":
                print("Option 2 Selected")
                break
            
            elif choice == "3":
                print("Option 3 Selected")
                break

            elif choice == "4":
                print("Exiting Account, Please come again!")
                exit()
                break

            else:
                print("Please try again.")
                continue

class Account:
    def __init__(self) -> None:
        #TODO add accountNumber, accountHolderName, rateOfInterest, and currentBalance as variables
        pass
        
    def getAccountNumber(self):
        #TODO create accessor method for accountNumber
        pass

    def getAccountHolderName(self):
        #TODO create accessor method for accountHolderName
        pass 

    def getRateOfInterest(self):
        #TODO create accessor method for rateOfInterest
        pass

    def getCurrentBalence(self):
        #TODO create accessor method for accountNumber
        pass

    def setAccountHolderName(self):
        #TODO create mutator method for accountHolderName
        pass

    def setRateOfInterest(self):
        #TODO create mutator method for rateOfInterest
        pass

    def Deposit(self):
        #TODO subtract money inputted from user from currentBalance
        pass

    def Withdraw(self):
        #TODO add money inputted from user to the currentBalance
        pass

class Bank:
    _bankName = "Bank of Canada"

    def openAccount(self):
        pass

    def searchAccount(self):
        #TODO Make it so that the account number is a parameter have the method find and return an account with the same account number
        pass

t = Application()

t.run()
#t.showMainMenu()