class ATM:
    def __init__(self,username,password,balance):
        self.username=username
        self.password=password
        self.balance=balance
    
    def login(self,name,password):
        if password == self.password: 
            if name == self.username:
                print("Security check completed!")
                return True
            else:
                print("Something wrong")
        else:
            print("Something is wrong")
    
    def display(self):
        print(f"You now have {self.balance}$ in your bank account")
    
    def deposit(self):
        ask1=int(input("How much do you want to deposit?"))
        if ask1>0:
            self.balance += ask1
            print(f"Now you have {self.balance}$")
        elif ask1 < 0:
            print("This is not supported!")
        elif ask1 == 0:
            pass
   
    def withdraw(self):
        ask2=int(input("How much money do you want to withdraw?"))
        if ask2 > self.balance:
            print("Insufficient money!")
        elif ask2 < self.balance:
            self.balance -= ask2
            print(f"Now you have {self.balance}$")
        else:
            pass
    
   