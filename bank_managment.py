
import os
import random
import sys
from colorama import Fore,Style,init

init(autoreset=True)

password = "7986"
attempt = 0

while attempt < 3:
    lock = input(Fore.LIGHTMAGENTA_EX+"Plz Enter Your password: ")
    if lock == password:
        print("--------------------------------")
        print(Fore.GREEN+"Welcome to your bank account")
        print("--------------------------------")
        break
    else:
        attempt += 1
        print("--------------------------------")
        print(Fore.YELLOW+"Wrong password")
        print("--------------------------------")

    if attempt == 3:
        print("---------------------------------------------------------")
        print(Fore.RED+"Sorry! You have used all attempts for your bank account")
        print("---------------------------------------------------------")
        sys.exit()
print(Style.BRIGHT+"=======STATE BANK OF INDIA=========")


class Bank:

    def __init__(self, Ifsc_code, Name, Father_name, Address, Gender, 
                mobile_number,deposit_amount, withdraw_amount):
        self.Account_Number = random.randint(100000000, 999999999)
        self.Ifsc_code = Ifsc_code
        self.Name = Name
        self.Father_name = Father_name
        self.address = Address
        self.Gender = Gender
        self.mobile_number = mobile_number
        self.Amount = random.randint(10000, 250000)
        self.deposit_amount = deposit_amount
        self.withdraw_amount = withdraw_amount
        
    def display(self):
        print(Fore.MAGENTA+"\n--------------------------------------------------")
        print(Fore.MAGENTA+f"Account Number:              {self.Account_Number}")
        print(Fore.MAGENTA+f"IFSC Code:                   {self.Ifsc_code}")
        print(Fore.MAGENTA+f"Name:                        {self.Name}")
        print(Fore.MAGENTA+f"Father's Name:               {self.Father_name}")
        print(Fore.MAGENTA+f"Address:                     {self.address}")
        print(Fore.MAGENTA+f"Gender:                      {self.Gender}")
        print(Fore.MAGENTA+f"Mobile Number:               {self.mobile_number}")
        print(Fore.MAGENTA+f"Amount:                      {self.Amount}")
        print(Fore.MAGENTA+f"----------------------------------------------------")

    def deposit(self):
        self.Amount += self.deposit_amount

    def withdraw(self):
        if self.withdraw_amount <= self.Amount:
           self.Amount -= self.withdraw_amount
        else:
            print(Fore.RED+"Sorry ! Insufiicent Balance")


class Client():

    def __init__(self):
        self.bank_client = []

    def add_client(self):

        Ifsc_code = (input(Fore.LIGHTMAGENTA_EX+"Enter Your IFSC Code: "))
        Name = input(Fore.LIGHTMAGENTA_EX+"Enter Your Name: ")
        Father_name = input(Fore.LIGHTMAGENTA_EX+"Enter Your Father name: ")
        Address = input(Fore.LIGHTMAGENTA_EX+"Enter Your Address: ")
        Gender = input(Fore.LIGHTMAGENTA_EX+"Enter Gender: ")
        mob = int(input("Enter mobile number client: "))
        Deposit = float(input(Fore.LIGHTMAGENTA_EX+f"Enter your Deposit Amount: "))
        Withdraw = float(input(Fore.LIGHTMAGENTA_EX+f"Enter your Withdraw Amount: "))

        s = Bank( 
                 Ifsc_code, 
                 Name,
                 Father_name,
                 Address,
                 Gender,
                 mob,
                 Deposit,
                 Withdraw
                 )
        
        s.deposit()
        s.withdraw()
        
        self.bank_client.append(s)

    def check_balance(self):
        acc = int(input(Fore.LIGHTMAGENTA_EX+"Enter Account number for a client: "))

        for client in self.bank_client:
            if client.Account_Number == acc:
                print(Style.BRIGHT+"\n======== Balance Details ========")
                print(Fore.LIGHTBLUE_EX+f"Name:                {client.Name}")
                print(Fore.LIGHTBLUE_EX+f"Account Number:      {client.Account_Number}")
                print(Fore.LIGHTBLUE_EX+f"Current Balance:     {client.Amount}")
                print(Fore.LIGHTBLUE_EX+f"----------------------------------------------")
                return

        print(Fore.RED+"Sorry! Account is not found")

    def history(self):
        acc_n = int(input(Fore.LIGHTMAGENTA_EX+"Enter Account number for a client: "))

        for client in self.bank_client:
            if client.Account_Number == acc_n:
                print(Style.BRIGHT+"\n======== Balance History ========")
                print(Fore.LIGHTYELLOW_EX+f"Name:                {client.Name}")
                print(Fore.LIGHTYELLOW_EX+f"Account Number:      {client.Account_Number}")
                print(Fore.LIGHTYELLOW_EX+f"Deposit Amount:      {client.deposit_amount}")
                print(Fore.LIGHTYELLOW_EX+f"Withdraw Amount:     {client.withdraw_amount}")
                print(Fore.LIGHTYELLOW_EX+f"Current Balance:     {client.Amount}")
                print(Fore.LIGHTYELLOW_EX+f"----------------------------------------------")
                return

        print(Fore.RED+"Sorry! Account is not found")

    def add_money(self):
        add_amount = int(input(Fore.LIGHTMAGENTA_EX+"Enter account number for a client: "))
        deposit_amount = float(input(Fore.LIGHTMAGENTA_EX+"Enter deposit amount: "))

        for client in self.bank_client:
            if client.Account_Number == add_amount:
                client.Amount += deposit_amount
                print(Style.BRIGHT+"\n===================Add Amount======================")
                print(Fore.GREEN+f"Name:                                {client.Name}")
                print(Fore.GREEN+f"Account Number:                      {client.Account_Number}")
                print(Fore.GREEN+f"Deposit Amount:                      {deposit_amount}")
                print(Fore.GREEN+f"Your Bank balance After Deposit is:  {client.Amount}")
                print(Fore.GREEN+f"------------------------------------------------------")
                return

        print(Fore.RED+"Sorry! Account is not found")

    def withdraw_money(self):
        withdraw_amount = int(input(Fore.LIGHTMAGENTA_EX+"Enter account number for a client: "))
        amount = float(input(Fore.LIGHTMAGENTA_EX+"Enter withdraw amount: "))

        for client in self.bank_client:
            if client.Account_Number == withdraw_amount:
                if amount <= client.Amount:
                    client.Amount -= amount
                    print(Style.BRIGHT+"\n===================Withdraw Amount======================")
                    print(Fore.CYAN+f"Name:                                {client.Name}")
                    print(Fore.CYAN+f"Account Number:                      {client.Account_Number}")
                    print(Fore.CYAN+f"Withdraw Amount:                     {amount}")
                    print(Fore.CYAN+f"Your Bank balance After Withdraw is: {client.Amount}")
                    print(Fore.CYAN+f"------------------------------------------------------")

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

    print(Fore.LIGHTCYAN_EX+"\n============BANK MANAGEMENT==============")
    print(Fore.LIGHTCYAN_EX+"\n============STATE BANK OF INDIA============")
    print(Fore.LIGHTGREEN_EX+"1. Add Client")
    print(Fore.LIGHTGREEN_EX+"2. show Client")
    print(Fore.LIGHTGREEN_EX+"3: check balance")
    print(Fore.LIGHTGREEN_EX+"4: Withdraw Money")
    print(Fore.LIGHTGREEN_EX+"5: Add Money")
    print(Fore.LIGHTGREEN_EX+"6: Balance History")
    print(Fore.LIGHTGREEN_EX+"7: Exit")

    choice = input(Fore.LIGHTMAGENTA_EX+"Enter a chioce: ")

    if choice == "1":

        client.add_client()

    elif choice == "2":

        client.show_client()

    elif choice == "3":
        client.check_balance()

    elif choice == "4":
        client.withdraw_money()

    elif choice == "5":
        client.add_money()

    elif choice == "6":
        client.history()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid choice!")
