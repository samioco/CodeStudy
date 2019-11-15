#BankAccountManager.py


class Account:
    # Define an __init__ constructor method with attributes shared by all accounts:
    def __init__(self,acct_nbr,opening_deposit):
        self.acct_nbr = acct_nbr
        self.balance = opening_deposit
    
    # Define a __str__ mehthod to return a recognizable string to any print() command
    def __str__(self):
        return f'${self.balance:.2f}'
    
    # Define a universal method to accept deposits
    def deposit(self,amount):
        self.balance += amount

    # Define a universal method to handle withdrawals
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(f'Funds Unavailable! Requested: ${amount} when Balance is only: ${self.balance}')


class Checking(Account):
    def __init__(self,acct_nbr,opening_deposit):
        # Run the base class __init__
        super().__init__(acct_nbr,opening_deposit)

    # Define a __str__ method that returns a string specific to Checking accounts
    def __str__(self):
        return f"Checking Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}"


class Savings(Account):
    def __init__(self,acct_nbr,opening_deposit):
        # Run the base class __init__
        super().__init__(acct_nbr,opening_deposit)

    # Define a __str__ method that returns a string specific to Savings accounts
    def __str__(self):
        return f"Savings Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}"


class Business(Account):
    def __init__(self,acct_nbr,opening_deposit):
        # Run the base class __init__
        super().__init__(acct_nbr,opening_deposit)

    # Define a __str__ method that returns a string specific to Business accounts
    def __str__(self):
        return f"Business Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}"



class Customer:
    def __init__(self, name, PIN):
        self.name = name
        self.PIN = PIN
        print(f"Created customer: {self.name}, PIN: {self.PIN}")
        
        # Create a dictionary of accounts, with lists to hold multiple accounts
        self.accts = {'C':[],'S':[],'B':[]}
        
    def __str__(self):
        #return f"{self.name} {self.accts}"
        return self.name
    
    def open_account(self,acct_type,acct_nbr,opening_deposit):
    	if acct_type=='C':
    		self.accts['C'].append(Checking(acct_nbr,opening_deposit))
    		print(f"{self.name} opened new checking account #{acct_nbr} ${opening_deposit}")
    	elif acct_type=='S':
    		self.accts['S'].append(Savings(acct_nbr,opening_deposit))
    		print(f"{self.name} opened new savings account #{acct_nbr} ${opening_deposit}")
    	elif acct_type=='B':
    		self.accts['B'].append(Business(acct_nbr,opening_deposit))
    		print(f"{self.name} opened new business account #{acct_nbr} ${opening_deposit}")
    	else:
    		print(f"Invalid account creation request: '{acct_type}'' not recognized.")

    def open_checking(self,acct_nbr,opening_deposit):
        self.accts['C'].append(Checking(acct_nbr,opening_deposit))
        print(f"{self.name} opened ")
    
    def open_savings(self,acct_nbr,opening_deposit):
        self.accts['S'].append(Savings(acct_nbr,opening_deposit))
        
    def open_business(self,acct_nbr,opening_deposit):
        self.accts['B'].append(Business(acct_nbr,opening_deposit))
    
    # rather than maintain a running total of deposit balances,
    # write a method that computes a total as needed
    def get_total_deposits(self):
        total = 0
        print(f"{self.name}'s Account Summary:")
        for acct in self.accts['C']:
            print(acct)
            total += acct.balance
        for acct in self.accts['S']:
            print(acct)
            total += acct.balance
        for acct in self.accts['B']:
            print(acct)
            total += acct.balance
        print(f"{self.name}'s Total Assets: ${total:.2f}\n")



def deposit(cust,acct_type,acct_num,amount):
    """
    make_dep(cust, acct_type, acct_num, amount)
    cust      = variable name (Customer record/ID)
    acct_type = string 'C' 'S' or 'B'
    acct_num  = integer
    amount   = integer
    """
    print(f"Received request to Deposit: {cust}|{acct_type}|{acct_num}|${amount}")
    for acct in cust.accts[acct_type]:
        if acct.acct_nbr == acct_num:
            acct.deposit(amount)
            if acct_type=='C':
            	print(f"{cust}: Checking Account# {acct_num} Deposit: ${amount}\n")
            elif acct_type=='S':
            	print(f"{cust}: Savings Account# {acct_num} Deposit: ${amount}\n")
            elif acct_type=='B':
            	print(f"{cust}: Business Account# {acct_num} Deposit: ${amount}\n")
    cust.get_total_deposits()


def withdraw(cust,acct_type,acct_num,amount):
    """
    make_dep(cust, acct_type, acct_num, amount)
    cust      = variable name (Customer record/ID)
    acct_type = string 'C' 'S' or 'B'
    acct_num  = integer
    amount    = integer
    """
    print(f"Received request to Withdraw: {cust}|{acct_type}|{acct_num}|${amount}")
    for acct in cust.accts[acct_type]:
        if acct.acct_nbr == acct_num:
            acct.withdraw(amount)
            if acct.balance>amount:
            	if acct_type=='C':
            		print(f"{cust}: Checking Account# {acct_num} Withdrawal: ${amount}\n")
            	elif acct_type=='S':
            		print(f"{cust}: Savings Account# {acct_num} Withdrawal: ${amount}\n")
            	elif acct_type=='B':
            		print(f"{cust}: Business Account# {acct_num} Withdrawal: ${amount}\n")
    cust.get_total_deposits()

def test():
	print("Running BankAccountManager test function...\n")
	bob = Customer('Bob',1)
	bob.open_account('C',123,150.25)
	bob.get_total_deposits()

	nancy = Customer('Nancy',2)
	nancy.open_account('B',2018,8900)
	nancy.get_total_deposits()

	#print(nancy)

	deposit(nancy,'B',2018,48.25)
	withdraw(nancy,'B',2018,100000)
	withdraw(nancy,'B',2018,500)


print("")
print("Bank Account Manager Exercise:")
print("Classes: Account, Checking, Savings, Business, Customer")
print("Functions: __init__, __str__, open accounts, withdraw, deposit, get_total_deposits")
print("")

test()