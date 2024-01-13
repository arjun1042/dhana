
import sys

class Customer:
    '''customer class to describe bank operations.....'''
    bankname="Andhra Bank"
    def __init__(self, name, balance=0.0):
        self.name=name
        self.balance=balance

    def deposite(self, amt):
        self.balance=self.balance+amt
        print('Balance after deposite', self.balance)

    def withdraw(self, amt):
        if amt > self.balance:
            print('Insufficient Funds........')
            sys.exit()
        self.balance=self.balance-amt
        print('Balance after withdraw:', self.balance)

print('Welcome to ', Customer.bankname)
name=input('Enter Your Name: ')
c=Customer(name)

while True:
    print('d- Deposit\nw - Withdraw\ne - Exit')
    option=input('choose your option:')
    
    if option.lower() == 'd':
        amount=float(input('Enter amount to diposite: '))
        c.deposite(amount)
        
    elif option.lower() == 'w':
        amount = float(input('Enter amount to withdraw: '))
        while amount % 500 != 0:
            print('Amount Should be multiples of 500')
            amount=float(input('Enter amount to diposite: '))
        c.withdraw(amount)
        
    elif option.lower() == 'e':
        print('Thanks For Banking')
        sys.exit()
        
    else:
        print('choose valid option')
        
