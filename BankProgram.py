"""
Author: Felipe Mena
Date: 05/11/2023
Description:
"""

listOfAcc = []

class Application:
    """The application class handles user interaction and UI display. This class acts as the hub for the the other classes"""

    def run(self):
        """This method calls showMainMenu starting the program"""
        self.showMainMenu()#creates an instance of main menu when called

    def showMainMenu(self):
        """
        This method displays 3 options in the console and allows the user to pick from them
        each choice produces a diffrent outcome        
        """
        #keeps users in a loop until they select from the options
        while True:
            print("___Welcome to Bank of Canada___\n\n<1> Select Account\n<2> Open Account\n<3> Exit\n") #displays options
            choice = input("Please select one of the available options: ") #takes user input

            #asks users for the account number and runs it through the searchAccount method. if the method returns an object, the showAccount Menu is called
            if choice == "1":
                print("Option 1 Selected")

                try:
                    accountSelect = int(input("Enter account number: "))
                except ValueError:
                    print("Please enter integer numbers.")
                    continue

                accountSelected = BoC.searchAccount(accountSelect)
                if accountSelected != False:
                    self.showAccountMenu(accountSelected)
                    break
            
            elif choice == "2":
                print("Option 2 Selected")

                try:
                    accNum = int(input("Please enter an account number (Integer Number): "))
                    accNames = input("Please enter your name (Text): ")
                    accROI = float(input("Enter a rate of interest (Decimal Number): "))
                    accBalance = int(input("Please enter your balance (Integer Number): "))
        
                    while True:
                        accType = input("Please enter account type (<1> Chequing <2> Savings <3> General): ")
                        if accType == "1" or accType == "2" or accType == "3":
                            break

                        print("Please select options 1, 2, or 3")
                        continue

                    if accType == "1":
                        accOverdraft = int(input("Please enter your overdraft limit: "))
                        BoC.openAccount(accNum, accNames, accROI, accBalance, accType, 0, accOverdraft)
                    
                    if accType == "2":
                        minBal = int(input("Please enter your minimum balance: "))
                        BoC.openAccount(accNum, accNames, accROI, accBalance, accType, minBal, 0)

                    else:
                        BoC.openAccount(accNum, accNames, accROI, accBalance, accType, 0, 0)


                except ValueError:
                    print("Error: Please enter correct value")

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
            print("\n___Account Menu___\n\n<1> Check Balance\n<2> Deposit\n<3> Withdraw\n<4> Exit Account\n")
            choice = input("Please select one of the available options: ")#takes user input

            #When this choice is selected it calls then displays getCurrentBalance method
            if choice == "1":
                print(f"Your accounts balance is: ${account.getCurrentBalance()}")
                continue
            
            #When this choice is selected the user is prompted for a number, that number is used as the parameter for the Deposit Method
            elif choice == "2":
                try:
                    userDeposAmount = int(input("How much money would you like to deposit: "))
                except ValueError:
                    print("Please enter integer numbers.")
                    continue
                account.Deposit(userDeposAmount)
                continue
            
            #When this choice is selected the user is prompted for a number, that number is used as the parameter for the Withdraw Method
            elif choice == "3":
                try:
                    userWithAmount = int(input("How much money would you like to withdraw: "))
                except ValueError:
                    print("Please enter integer numbers.")
                    continue
                account.Withdraw(userWithAmount)
                continue

            #exits the program
            elif choice == "4":
                print("Exiting Account, Please come again!")
                exit()
            
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



App = Application()
BoC = Bank()

g1 = Account(1111, "Felipe", 0.5, 5000)
g2 = Account(2222, "Komail", 0.5, 100000)

App.run()