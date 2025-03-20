class account:
    total_deposits = 0
    total_withdrawals = 0
            
    def __init__(self,username, password , balance=0.0):
        self._username = username
        self._password = password
        self._balance = balance
    
            
    def login(self, username, password):
        if self._username == username and self._password == password:
            print(f"Login Successful! Welcome, {self._username}.")
            return True
        else:
            raise ValueError("Invalid Login Credentials")
    
            
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.total_deposits += 1
            print(f"Amount deposited: ${amount}. New balance: ${self._balance}")
            print("Thank you for depositing...")
        else:
            print("Deposit amount must be greater than 0.") 
    
            
    def check_deposit(self):
        print(self.total_deposits)
               
                
    def withdrawals(self, withdraw):
        if withdraw > 0 and withdraw <= self._balance:
            self._balance -= amount
            self.total_withdrawals 
            print(f"Withdrew ${amount}. Remaining Balance: ${self._balance}")
        else:
            print("Insufficient funds or invalid amount")
    
            
    def total_withdrawals(self):
        print(self.total_withdrawals)
    
       
    def get_balance(self):
        return self._balance
    
    
    def logout(self):
        print(f"{self._username} has logged out.")
        
class savingsaccount(account):
    def __init__(self, username, password, balance=0, interest_rate=0.03):
        super().__init__(username, password, balance)
        self._interest_rate = interest_rate
        
    def calculate_interest(self):
        interest = self._balance * self._interest_rate
        print(f"Interest earned: ${interest}")
        return interest
    
    def account_type(self):
        return "Savings Account"
    
class checkingaccount(account):
    def __init__(self, username, password, balance=0.0, overdraft_limit=100):
        super().__init__(username, password, balance)
        self._overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > 0 and (self._balance + self._overdraft_limit) >= amount:
            self._balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self._balance}")
        else:
            print("Insufficient funds (Overdraft limit exceeded).")
    
    def account_type(self):
        return "Checking Account"
    
    

print("Welcome to Anilton Trade Bank!")
username = input("Enter a username: ")
password = input("Enter a password: ")

account_choice = input("Choose account type (Savings/Checking): ").strip().title()

if account_choice == "Savings":
    account = savingsaccount(username, password)
    print(f"{account_choice} account created successfully!!")
elif account_choice == "Checking":
    account = checkingaccount(username, password)
    print(f"{account_choice} account created successfully!!")
else:
    print("Invalid account type. Exiting program.")
    exit()

# --- User Login ---
print("\nLog in to Your Account:")
login_user = input("Username: ")
login_pass = input("Password: ")


if account.login(login_user, login_pass):
    print(f"You are logged into your {account.account_type()}")      
                   
    while True:
        print("\nBanking Services")
        print("\n1.) Withdrawals \n2.) Deposits \n3.) View account balance \n4.) Calculate interest (Only Savings Account) \n5.) View total withdrawals \n6.) View total deposits \n7.) Quit \n")
        option_choice = int(input("Enter service choice: "))
            
        if option_choice == 1:
            amount = float(input("Enter withdrawal amount: "))
            account.withdrawals(amount)
        elif option_choice == 2:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif option_choice == 3:
                print(f"Your account balance is ${account._balance}")
        elif option_choice == 4 and isinstance(account, savingsaccount):
                account.calculate_interest()
        elif option_choice == 5:
                print(f"Total withdrawals: {account.total_withdrawals}")
        elif option_choice == 6:
                print(f"Total deposits: {account.total_deposits}")    
        elif option_choice == 7:
                print("Thank you for using Anilton Trade Bank.")
                account.logout
                break
        else:
                print("Invalid Option!!. Try again.")
                
