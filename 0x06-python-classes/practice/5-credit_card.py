#!/usr/bin/python3
class CreditCard:
    """Credit card class """
    def __init__(self, name, acnt, bank, limit, balance=0):
        """Instantiate the object of CreditCard class

        Args:
            name (str)      -> Name of the client
            account(str)    -> Account Number of the client, this cant be changed once assinged
            bank(str)       -> The Bank Branch of the clinet
            limit(int)      -> The spending limit on the credit card
            balance(int)    -> The balance on the card, by default a CC has a 0 balance
        """
        self.__name = name
        self.__account = acnt
        self.__bank = bank
        self.__limit = limit
        self.__balance = balance

    @property
    def name(self):
        """Get the name of the client"""
        return self.__name
    
    @name.setter
    def name(self, new_name):
        """Mutate the name of the client, for some reason
        
        Args:
            new_name (str) -> the new name
        """
        self.name = new_name

    @property
    def account(self):
        """Get the account number"""
        return self.__account

    @property
    def bank(self):
        """Get the branch of the client"""
        return self.__bank
    
    @bank.setter
    def bank(self, bank):
        """Change branch to another branch
        
        Args:
            bank (str) -> the new branch
        """
        if self.__bank != bank:
            self.__bank = ban
            return ("Switched branch from to {}".format(bank))
        else:
            return "Cannot Switch to the same branch"
    
    @property
    def limit(self):
        """Get the limit of the card"""
        return self.__limit

    @limit.setter
    def limit(self, increment):
        """Increment the current limit by increment

        Args:
            increment (int) -> the value to be added to current limit
        """
        try:

            if (not isinstance(increment, int)):
                raise TypeError("Can only increment by a number")
            if increment == 0:
                raise ValueError("Cannot Increment by Zero")
            else:
                self.__limit += increment
                return True

        except Exception as e:
            return (e)

    @property
    def balance(self):
        """Check card balance"""
        return self.__balance


    @balance.setter
    def charge(self, amount):
        """Charge some amount from the credit card"""
        if not (isinstance(amount, int)):
            raise TypeError("Damn it! You are supposed to charge money not {}".format(amount))
            return 
        else:
            self.__balance -= amount
            return True

cc = CreditCard("John Doe", "123-2422-3234", "Carlifornia Savings", 1000, 204)
