import sys

balance = 10000
minimum  = 500

password = "5887"
attempt = 0

while attempt < 3:
    lock = input("Enter Your Password: ")
    if lock == password:
        print("login succesfully!")
        break
    else:
        attempt += 1
        print("Wrong password") 
      
    if attempt == 3:
        print("Account locked! you have used all 3 attempt")  
        sys.exit()

while True:
    print("\n ===ATM Main Menu===")
    # print("1. Enter your password")
    print("2. Check balance")
    print("3. Deposit Money")
    print("4. Withdraw money")
    print("5. Exit")

    choice = input("Please select an option: ")


# process choice check balance 
   
    if choice == "2":
        print("current balance: ", balance)

    elif choice == "3":
       amount = float(input("Enter the deposit amount: "))
       if amount > 0:
           balance += amount
           print("Deposit Succesful!")
           print("New balance: ", balance)
       else:
             print("Invalid Amount")

    elif choice == "4":
        amount = float(input("Enter the withdraw amount: "))

        if balance - amount >= minimum:
            balance -= amount
            print("Withdraw Succesfully! ")
            print("Reameaning balance", balance)
        else:
            print("withdraw failed")
            print("Your account balance maintaned", balance)

    elif choice == "5":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice Please try again later")

                      
    