balance=0
def check_balance():
    print("total balance:",balance)

def deposit(amt):
    global balance
    balance = balance + amt
    print(amt,"rs.deposit.")

def withdraw(amt):
    global balance
    balance = balance-amt  
    print(amt,"rs.withdraw.")

while True:
    choice=int(input("\enter choice:\n1.deposi cash\t2.withdraw cash\n3.check_balance\t4 exit"))
    match choice:
        case 1 :
            print("deposit cash")
            d_amt=int(input("enter amount to deposit:"))
            deposit(d_amt)
        case 2:
            print("withdraw cash")
            w_amt=int(input("enter amount to withdraw:"))
            withdraw(w_amt)
        case 3:
            print("check balance")
            check_balance()
        case 4:
            print("exiting")
            break
        case _:
            print("invalid choice")

         
