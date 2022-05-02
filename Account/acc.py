class Account:
    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())


    def withdraw(self, amount):
        self.balance=self.balance - amount
        
    def deposit(self, amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    '''This class generates checking account objects'''  #Doc strings

    type="checking" #class variable
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee #instance variable

checking = Checking("Object Oriented Programming in Python/Account/balance.txt", 1) #object instance
#checking.deposit(10)
#print(checking.balance)
checking.transfer(100)
print(checking.balance)
checking.commit()

#account = Account("Object Oriented Programming in Python//Account//balance.txt") #in place of "filepath"
#account is an object of class Account, helping us to call the class

