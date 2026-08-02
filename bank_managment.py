
import os
import random
import sys

password = "7986"
attempt = 0

while attempt < 3:
    lock = input("Plz Enter Your password: ")
    if lock == password:
        print("Welcome to your bank account")
        break
    else:
        attempt += 1
        print("Wrong password")

    if attempt == 3:
        print("Sorry! You have used all attempts for your bank account")
        sys.exit()


class Bank:

    def __init__(self, Account_Number, Ifsc_code, Name, Father_name, Address, Gender,
                 deposit_amount, withdraw_amount):
        self.Account_Number = Account_Number
        self.Ifsc_code = Ifsc_code
        self.Name = Name
        self.Father_name = Father_name
        self.address = Address
        self.Gender = Gender
        self.Amount = random.randint(10000, 25000)
        self.deposit_amount = deposit_amount
        self.withdraw_amount = withdraw_amount
        
    def display(self):
        print("\n--------------------------------------------------")
        print(f"Account Number:              {self.Account_Number}")
        print(f"IFSC Code:                   {self.Ifsc_code}")
        print(f"Name:                        {self.Name}")
        print(f"Father's Name:               {self.Father_name}")
        print(f"Address:                     {self.address}")
        print(f"Gender:                      {self.Gender}")
        print(f"Amount:                      {self.Amount}")
        print(f"----------------------------------------------------")

    def deposit(self):
        self.Amount += self.deposit_amount

    def withdraw(self):
        if self.withdraw_amount <= self.Amount:
           self.Amount -= self.withdraw_amount
        else:
            print("Sorry ! Insufiicent Balance")


class Client():

    def __init__(self):
        self.bank_client = []

    def add_client(self):

        Account_Number = int(input("Enter Your Account Number: "))
        Ifsc_code = (input("Enter Your IFSC Code: "))
        Name = input("Enter Your Name: ")
        Father_name = input("Enter Your Father name: ")
        Address = input("Enter Your Address: ")
        Gender = input("Enter Gender: ")
        Deposit = float(input(f"Enter your Deposit Amount: "))
        Withdraw = float(input(f"Enter your Withdraw Amount: "))

        s = Bank(Account_Number, 
                 Ifsc_code, 
                 Name,
                 Father_name,
                 Address,
                 Gender,
                 Deposit,
                 Withdraw)
        
        s.deposit()
        s.withdraw()
        
        self.bank_client.append(s)

    def check_balance(self):
        acc = int(input("Enter Account number for a client: "))

        for client in self.bank_client:
            if client.Account_Number == acc:
                print("\n======== Balance Details ========")
                print(f"Name:                {client.Name}")
                print(f"Account Number:      {client.Account_Number}")
                print(f"Current Balance:     {client.Amount}")
                print(f"----------------------------------------------")
                return

        print("Sorry! Account is not found")

    def history(self):
        acc_n = int(input("Enter Account number for a client: "))

        for client in self.bank_client:
            if client.Account_Number == acc_n:
                print("\n======== Balance History ========")
                print(f"Name:                {client.Name}")
                print(f"Account Number:      {client.Account_Number}")
                print(f"Deposit Amount:      {client.deposit_amount}")
                print(f"Withdraw Amount:     {client.withdraw_amount}")
                print(f"Current Balance:     {client.Amount}")
                print(f"----------------------------------------------")
                return

        print("Sorry! Account is not found")

    def add_money(self):
        add_amount = int(input("Enter account number for a client: "))
        deposit_amount = float(input("Enter deposit amount: "))

        for client in self.bank_client:
            if client.Account_Number == add_amount:
                client.Amount += deposit_amount
                print("\n===================Add Amount======================")
                print(f"Name:                                {client.Name}")
                print(f"Account Number:                      {client.Account_Number}")
                print(f"Deposit Amount:                      {deposit_amount}")
                print(f"Your Bank balance After Deposit is:  {client.Amount}")
                print(f"------------------------------------------------------")
                return

        print("Sorry! Account is not found")

    def withdraw_money(self):
        withdraw_amount = int(input("Enter account number for a client: "))
        amount = float(input("Enter withdraw amount: "))

        for client in self.bank_client:
            if client.Account_Number == withdraw_amount:
                if amount <= client.Amount:
                    client.Amount -= amount
                    print("\n===================Withdraw Amount======================")
                    print(f"Name:                                {client.Name}")
                    print(f"Account Number:                      {client.Account_Number}")
                    print(f"Withdraw Amount:                     {amount}")
                    print(f"Your Bank balance After Withdraw is: {client.Amount}")
                    print(f"------------------------------------------------------")

                elif withdraw_amount > client.Amount:
                    print("Sorry! Insufficient Balance")
                else:
                    print("Sorry! Insufficient Balance")
                return

        print("Sorry! Account is not found")


    def show_client(self):

        if len(self.bank_client) == 0:
            print("\n No Client Found")
            return

        for i in self.bank_client:
            i.display() 


        
client = Client()

while True:

    print("\n============BANK MANAGEMENT==============")
    print("\n============STATE BANK OF INDIA============")
    print("1. Add Client")
    print("2. show Client")
    print("3: check balance")
    print("4: Balance History")
    print("5: Add Money")
    print("6: Exit")

    choice = input("Enter a chioce: ")

    if choice == "1":

        client.add_client()

    elif choice == "2":

        client.show_client()

    elif choice == "3":
        client.check_balance()

    elif choice == "4":
        client.history()

    elif choice == "5":
        client.add_money()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid choice!")
