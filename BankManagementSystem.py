from abc import ABC, abstractmethod

class account(ABC):
    def __init__(self, acc_num : int, customer_name, balance : float):
        self._acc_num = acc_num
        self._balance = balance
        self.customer_name = customer_name
        
    @abstractmethod
    def account_type(self):
        pass

    def get_balance(self):
        return self._balance

    def get_acc_num(self):
        return self._acc_num
    
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited: Rs. {amount}     Current Balance: Rs. {self._balance}")
    
    def withdraw(self, amount):
        if amount > self._balance:
            print(f"Sorry! but your {self._acc_num} has insufficient funds")
        
        else:
            self._balance -= amount
            print("Amount withdrawl done successfully!")
            print(f"\nWithdrew: Rs. {amount}     Current Balance: Rs. {self._balance}")
    
class Savings_account(account):
    def __init__(self, acc_num : int, customer_name, balance : float, interest_rate :  float): 
        super().__init__(acc_num, customer_name, balance)
        self._interest_rate = interest_rate
    
    def account_type(self):
        return f'Savings Account'
    
    def apply_interest(self):
        interest = self._balance * self._interest_rate / 100
        self.deposit(interest)
        print(f"Interest of {interest}% is applied to {self._acc_num}.     New Balance: Rs. {self._balance}")
        
class current_account(account):
    def __init__(self, acc_num : int, customer_name, balance : float, overdraft_limit):
        super().__init__(acc_num, customer_name, balance)
        self.__overdraft_limit = overdraft_limit
    
    def account_type(self):
        return f"Current Account"
    
    def set_overdraft_limit(self, limit : float):
        self.__overdraft_limit = limit
        print(f"Overdraft limit set to {self.__overdraft_limit}")
        
def display_account_info(acc : account):
    print(f"Account Number: {acc.get_acc_num()}")
    print(f"Account Holder Name: {acc.customer_name}")
    print(f"Account Type: {acc.account_type()}")
    print(f"Balance: Rs. {acc.get_balance()}")
    
c1 = Savings_account(101, 'Manasi', 1000, 3)
c2 = current_account(201, 'Mitali', 5000, 1500)

display_account_info(c1)
display_account_info(c2)

c1.deposit(500)
c1.withdraw(200)
c1.apply_interest()

c2.deposit(1000)
c2.withdraw(3000)
c2.set_overdraft_limit(2000)

display_account_info(c1)
display_account_info(c2)