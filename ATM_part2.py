from ATM_part1 import ATM 
acc = ATM("Arti",3005,1500)

while True:
    usrn=input("Enter username:  ")
    passw=int(input("Enter password:"))
    acc1=acc.login(usrn,passw)
    if acc1 == False:
        break
    if acc1== True:
        while True:
            print("Please follow the same format as the function below!")
            ask3= int(input("""Do you want to:
            Display; Deposit; Withdraw or Exit? 
            """))
            if ask3 == "Display":
                acc.display()
            elif ask3 == "Deposit":
                acc.deposit()
            elif ask3 == "Withdraw":
                acc.withdraw()
            elif ask3 == "Exit":
                break
            else:
                print("Not supported answer!")
    

