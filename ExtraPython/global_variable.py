'''
balance = 0

def main():
    print("Balance: ", balance)
    deposite(100)
    withdraw(50)
    print("Current Balance: ", balance)
    
def deposite(n):
    global balance
    balance += n
    
def withdraw(n):
    global balance
    balance -= n
    
if __name__ == "__main__":
    main() 
'''

'''
class Account:
    def __init__(self):
        self._balance = 0
        
# In classes the Variable is accesable to all the functions because we are accessing it by parameter self 
        
    @property
    def balance(self):
        return self._balance
    
    def deposite(self, n):
        self._balance +=n
        
    def withdraw(self, n):
        self._balance -= n
        
def main():
    account = Account()  #Object #Constructor
    print("Balance:", account.balance)
    account.deposite(100)
    account.withdraw(50)
    print("Balance:", account.balance)
    
if __name__ == "__main__":
    main()
'''