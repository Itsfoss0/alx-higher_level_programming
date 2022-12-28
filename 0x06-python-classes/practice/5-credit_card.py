#!/usr/bin/python3
class CreditCard:
    """Credit card class """
    def __init__(self, name, acnt, bank, limit, balance=0):
        """Instantiate the object of CreditCard class

        Args:
            name (str)      -> Name of the client
            account(str)    -> Account Number of the client
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
    

