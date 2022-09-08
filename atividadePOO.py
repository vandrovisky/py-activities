from http import client
import re
from abc import ABC, abstractclassmethod


class People:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @name.setter
    def name(self,name):
        self._name = name.title()
    
    @age.setter
    def age(self, age):
        self._age = int(age)


class Client(People): 
    def __init__(self, name, age):
        super().__init__(name, age)
        self.account = None
    
    def insert_account(self, account):
        self.account = account


class Account(ABC):
    def __init__(self, agency, id_account):
        self.agency = agency 
        self.id_account = id_account
        self.sale = 0
    
    @property
    def agency(self):
        return self._agency
    
    @agency.setter
    def agency(self, agency):
        self._agency = str(agency)

    @property
    def id_account(self):
        return self._id_account

    @id_account.setter
    def id_account(self, id_account):
        self._id_account = str(id_account)


    def deposit(self, value):
        self.sale += value
        self.details()

    def details(self):
        print(f'Agency: {self.agency}')
        print(f'ID: {self.id_account}')
        print(f'Sale: {self.sale}')

  
    @abstractclassmethod
    def draw(self, value):
        pass


class SavingsAccount(Account):
    def draw(self, value):
        if self.sale < value:
            print('Saldo insuficiente')
            return

        self.sale -= value
        self.details()   


class CurrentAccount(Account):
    def __init__(self, agency, id_account, limit = 500):
        super().__init__(agency, id_account)
        self.limit = limit

    def draw(self, value):
        if (self.sale + self.limit) < value:
            print('Saldo insuficiente')
            return

        self.sale -= value
        self.details()   


class Bank:
    def __init__(self):
        self.agencies = ['0001','1002','1022']
        self.clients = []
        self.accounts = []

    def insert_clients(self, client):
        self.clients.append(client)

    def insert_accounts(self, accounts):
        self.accounts.append(accounts)

    def authenticate(self, client):
        if client not in self.clients:
            return False
       
        if client not in self.accounts: 
            return False
        
        if client.account.agency not in self.agencies:
            return False

        return True

if __name__ == '__main__':
    pass