"""
Author: Felipe Mena
Date: 05/11/2023
Description:
"""

listOfAcc = []

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
    #initalizes variables for account, adds itself into a list of objects
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBal):
        self._accountNumber = accountNumber
        self._accountHolderName = accountHolderName
        self._rateOfInterest = rateOfInterest
        self._currentBal = currentBal
        listOfAcc.append(self)

    #Accessor method for account number
    def getAccountNumber(self):
        return self._accountNumber

    #Accessor method for account holder name
    def getAccountHolderName(self):
        return self._accountHolderName

    #Accessor method for rate of interest
    def getRateOfInterest(self):
        return self._rateOfInterest

    #Accessor method for current balence
    def getCurrentBalence(self):
        return self._currentBal
    
    #Mutator method for accountHolderName
    def setAccountHolderName(self, newAccName):
        self._accountHolderName = newAccName

    #Mutator method for rateOfInterest
    def setRateOfInterest(self, newROI):
        self._rateOfInterest = newROI

    def Deposit(self, amount):
        if amount <= 0:
            print("Value depositied must be greater then zero, transaction failed.")
            return False
        self._currentBal += amount
        print("Transaction successful.")
        return True

    def Withdraw(self, amount):
        if amount > self._currentBal or amount <= 0 :
            print("Amount cannot be more then current balence or negative, transaction failed.")
            return False
        self._currentBal -= amount
        print("Transaction successful.")
        return True


class Bank:
    _bankName = "Bank of Canada"

    #this method takes each field variable needed to make a Account object as a parameter and creates a instance of the Account object
    def openAccount(self, accountNum, accName, ROI, accBal):
        newAcc = Account(accountNum, accName, ROI, accBal)
        return newAcc

    #this methods sifts through each object in the list of objects and returns true if found, returns false if nothing is found
    def searchAccount(self, accountNumber):
        for obj in listOfAcc:
            if accountNumber == obj._accountNumber:
                print("Account successfully found.")
                return True
        print("Failed to find account.")
        return False


t = Application()
b = Bank()

#t.run()
g1 = Account(1111, "Felipe", 0.5, 500)
g1.Deposit(500)
g1.Deposit(-20)

print(g1.getCurrentBalence())

g1.Withdraw(500)
g1.Withdraw(200000)
g1.Withdraw(-2)

print(g1.getCurrentBalence())
#t.showMainMenu()