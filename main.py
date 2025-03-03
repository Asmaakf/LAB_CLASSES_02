from bankAccount import BankAccount


print("----------------------------------------")
print("              Bank System")
print("----------------------------------------")

# Holders 
try:
    # Holder1
    holder1 = BankAccount("Asmaa", 2000)
    #holder1 = BankAccount("Asmaa", "2000") # Exception balance amount must be intger number
    #holder1 = BankAccount(10, 2000) # Exception holder name must be sting
    
    print(f"Welcome {holder1.get_account_holder()} to our system!!")
    print("----------------------------------------")
    print("User infomations: ")
    print(f"User name: {holder1.get_account_holder()} | Currunt balance: {holder1.get_balance()}")
    print("-----")
    try:
        print("Deposit & Withdraw processes:")
        # Deposit 500 to holder1 2000 + 500 = 2500
        print(f"Before deposit process: {holder1.get_balance()}")
        holder1.deposit(500)
        print(f"After deposit process: {holder1.get_balance()}")
        print("-----")
        # Withdraw 600 from holder1 2500 - 600 = 1900
        print(f"Before withdraw process: {holder1.get_balance()}")
        holder1.withdraw(600)
        print(f"After withdraw process: {holder1.get_balance()}")
    except Exception as e:
        print(e)

    print("-----")
    print(f"{holder1.get_account_holder()} your balance was updated {holder1.get_balance()}.")
    print("----------------------------------------")
        
    # Holder2 
    holder2 = BankAccount("Ahmad")
    print(f"Welcome {holder2.get_account_holder()} to our system!!")
    print("----------------------------------------")
    print("User infomations: ")
    print(f"User name: {holder2.get_account_holder()} | Currunt balance: {holder2.get_balance()}")
    print("-----")

    try:
        print("Deposit & Withdraw processes:")
        # Deposit 100 to holder2 0 + 100 = 100
        print(f"Before deposit process: {holder2.get_balance()}")
        holder2.deposit(100)
        print(f"After deposit process: {holder2.get_balance()}")
        print("-----")
        # Withdraw 200 from holder2 100 - 200 = -100  insufficient exception
        print(f"Before withdraw process: {holder2.get_balance()}")
        holder2.withdraw(200)
        print(f"After withdraw process: {holder2.get_balance()}")
    except Exception as e:
        print(e)

    print("-----")
    print(f"{holder2.get_account_holder()} your balance was updated {holder2.get_balance()}.")
    print("----------------------------------------")
except Exception as e:
    print(e)


