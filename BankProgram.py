"""
Author: Felipe Mena
Date: 05/11/2023
Description:
"""

import random

print()
listOfAcc = []

def Prompt(inPrompt, type):
    """
    the Prompt function creates input statements with built in exception handling
    inPrompt: this paramater is the text that goes into the 
    type: this parameter determines the type that the input statement is converted into
    return: returns the input value
    """
    while True:
        try:
            question = type(input(inPrompt))
            return question
        
        except ValueError:
            print("Please enter the correct data.")
            continue
    


class Application:
    """The application class handles user interaction and UI display. This class acts as the hub for the the other classes"""

    def run(self, bank):
        """
        This method calls showMainMenu starting the program
        bank: takes in the name of the Bank class object allowing the application class to use Bank class features
        """
        self.showMainMenu(bank)#creates an instance of main menu when called

    def showMainMenu(self, bank):
        """
        This method displays 3 options in the console and allows the user to pick from them each choice produces a diffrent outcome
        bank: takes in the name of the Bank class object allowing the application class to use Bank class features      
        """
        #keeps users in a loop until they select from the options
        while True:
            print("\n___Welcome to Bank of Canada___\n\n<1> Select Account\n<2> Open Account\n<3> Exit\n") #displays options
            choice = input("Please select one of the available options: ") 

            #asks users for the account number and runs it through the searchAccount method. if the method returns an object, the showAccount Menu is called
            if choice == "1":
                print("\nAccount Search")

                accountSelect = Prompt("Enter account number: ", int)

                accountSelected = bank.searchAccount(accountSelect)
                if accountSelected != False:
                    self.showAccountMenu(accountSelected)
                    break
            
            #this block creates accounts asking users for the information required to make an account and using the results as the parameters for the openAccount Method
            elif choice == "2":
                print("\nCreate Account")

                accNum = random.randint(1,9999) #generates a random number as the accNum value
                print(f"Your account number is {accNum}")
                accNames = Prompt("Please enter your name (Text): ", str)
                accROI = Prompt("Enter a rate of interest (Decimal Number): ", float)
                accBalance = Prompt("Please enter your balance (Integer Number): ", int)

                #this while loop keeps users locked in until they select a correct value
                while True:
                    accType = input("Please enter account type (<1> Chequing <2> Savings <3> General): ")
                    if accType == "1" or accType == "2" or accType == "3":
                        break

                    print("Please select options 1, 2, or 3")
                    continue

                #these statements ask diffrent questions based on account type and call openAccount using inputted values 
                if accType == "1":
                    accOverdraft = Prompt("Please enter your overdraft limit: ", int)
                    bank.openAccount(accNum, accNames, accROI, accBalance, accType, 0, accOverdraft)

                if accType == "2":
                    minBal = Prompt("Please enter your minimum balance: ", int)
                    bank.openAccount(accNum, accNames, accROI, accBalance, accType, minBal, 0)

                else:
                    bank.openAccount(accNum, accNames, accROI, accBalance, accType, 0, 0)
                continue
            
            #exits the program
            elif choice == "3":
                print("Exiting Bank of Canada, Have a good day!")
                exit()

            #continues loop if one of the options isnt selected
            else:
                print("Please try again.")
                continue

    def showAccountMenu(self, account):
        """
        This method displays 4 options and allows the user to pick from them
        each choice produces a diffrent outcome
        """

        #This loop keeps the user inside of it until they input one of the available options 
        while True:
            print("\n___Account Menu___\n\n<1> Check Balance\n<2> Deposit\n<3> Withdraw\n<4> Return to Main Menu\n")
            choice = input("Please select one of the available options: ")#takes user input

            #When this choice is selected it calls then displays getCurrentBalance method
            if choice == "1":
                print(f"Your accounts balance is: ${account.getCurrentBalance()}")
                continue
            
            #When this choice is selected the user is prompted for a number, that number is used as the parameter for the Deposit Method
            elif choice == "2":
                userDeposAmount = Prompt("How much money would you like to deposit: ", int)
                account.Deposit(userDeposAmount)
                continue
            
            #When this choice is selected the user is prompted for a number, that number is used as the parameter for the Withdraw Method
            elif choice == "3":
                userWithAmount = Prompt("How much money would you like to withdraw: ", int)
                account.Withdraw(userWithAmount)
                continue

            #exits the program
            elif choice == "4":
                print("Exiting Account, Returning to Main Menu!")
                self.showMainMenu()
            
            #continues loop if one of the options isnt selected
            else:
                print("Please try again.")
                continue

class Account:
    """
    This class handles the business logic of the program, the class contains banking information and the math for depositing and withdrawing
    """

    #initalizes variables for account, adds itself into a list of objects
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBal):
        self._accountNumber = accountNumber
        self._accountHolderName = accountHolderName
        self._rateOfInterest = rateOfInterest
        self._currentBal = currentBal
        listOfAcc.append(self)#adds an instance of the class into a list

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
    def getCurrentBalance(self):
        return self._currentBal
    
    #Mutator method for accountHolderName
    def setAccountHolderName(self, newAccName):
        self._accountHolderName = newAccName

    #Mutator method for rateOfInterest
    def setRateOfInterest(self, newROI):
        self._rateOfInterest = newROI

    def Deposit(self, amount):
        """
        The deposit method takes the the parameter amount and adds it to the current balence. If the amount is 0 or lower the transaction fails Returns true or false based on transaction succes
        """
        if amount <= 0:
            print("Value depositied must be greater then zero, transaction failed.")
            return False
        
        self._currentBal += amount
        print("Transaction successful.")
        return True
    
    def Withdraw(self, amount):
        """
        #The deposit method takes the the parameter amount and adds it to the current balence. If the amount is 0 or lower or greater then current balence the transaction fails Returns true or false based on transaction success
        """
        if amount > self._currentBal or amount <= 0 :
            print("Amount cannot be more then current balence or negative, transaction failed.")
            return False
        
        self._currentBal -= amount
        print("Transaction successful.")
        return True


class Bank:
    """
    The Bank class handles the logic of creating and searching accounts 
    """
    _bankName = "Bank of Canada"

    
    def openAccount(self, accountNum, accName, ROI, accBal, type, minBal, overDraft):
        """this method takes each field variable needed to make a Account object as a parameter and creates a instance of the Account object"""
        if type == "1":
            newAcc = ChequingAccount(accountNum, accName, ROI, accBal, overDraft)

        if type == "2": 
            newAcc = SavingsAccount(accountNum, accName, ROI, accBal, minBal)
    
        else:
            newAcc = Account(accountNum, accName, ROI, accBal)
    
        return newAcc

   
    def searchAccount(self, accountNumber):
        """
        this methods takes accountNumber as a parameter, the method sifts a list of all bank objects. If accountNumber 
        matches the account number of an object the returns, returns false if nothing is found
        """
        for obj in listOfAcc:
            if accountNumber == obj._accountNumber:
                print("Account successfully found.")
                return obj
        print("Failed to find account.")
        return False

class SavingsAccount(Account):
    """This class inherets the Account method and changes the init and Withdraw method"""

    #inherets the init method from accoount and adds a new variable called minimumBalance
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBal, minimumBalance):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBal)
        self._minimumBalance = minimumBalance
    
    def Withdraw(self, amount):
        """
        This class inherits the withdraw method from the Bank class and overrides it. This withdraw method checks for the objects minumum balance and checks if the 
        money withdrawn will go under that minimum balance if it does the transaction fails. Returns true or false based on transaction success
        """
        if self._currentBal - amount < self._minimumBalance:
            print("The amount withdrawn will go under your minimum balance, transaction failed.")
            return False
        return super().Withdraw(amount)
    
class ChequingAccount(Account):
    """This class inherets the Account method and changes the init and Withdraw method"""

    #inherets the init method from accoount and adds a new variable called overdraft
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBal, overDraft):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBal)
        self._overDraft = overDraft

    def Withdraw(self, amount):
        """#this method overides the Account class withdraw method. This withdraw allows the user to go under their minimum balance by an amount = to the overDraft variable. Other then that works the same as the withdraw method from Account."""
        if amount > self._currentBal + self._overDraft or amount <= 0 :
            print("Hit limit on overdraft, transaction failed, or negative number entered")
            return False
        
        self._currentBal -= amount
        print("Transaction sucecessful")
        return True