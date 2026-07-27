kal ismei deposit and withdraw ko add karenge or minimum balance bhi

import os
import sys

password = "7986"
attemt = 0

while attemt < 3:
    lock = input("Plz Enter Your password: ")
    if lock == password:
        print("Welcome to your bank account")
        break
    else: 
         attemt += 1
         print("Wrong password")

    if attemt == 3:
        print("Sorry! You have use all attmpts in your bank account")

        sys.exit()


class Bank():
    Amount = 15000

    def __init__(self,Account_Number,Isfc_code,Name,Father_name,address):
        self.Account_Number = Account_Number
        self.Ifsc_code = Isfc_code
        self.Name = Name
        self.Father_name = Father_name
        self.address = address
        

    def display(self):
        print("\n--------------------------------------------------")
        print(f"Account Number:              {self.Account_Number}")
        print(f"IFSC Code:                   {self.Ifsc_code}")
        print(f"Name:                        {self.Name}")
        print(f"Father's Name:               {self.Father_name}")
        print(f"Address:                     {self.address}")
        print(f"Amount:                      {self.Amount}")
        print(f"----------------------------------------------------")

class Client():

    def __init__(self):
        self.bank_client = []

    def add_client(self):

        Account_Number = int(input("Enter Your Account Number: "))
        Ifsc_code = (input("Enter Your IFSC Code: "))
        Name = input("Enter Your Name: ")
        Father_name = input("Enter Your Father name: ")
        Address = input("Enter Your Address: ")
        # Amount = float(input("Enter Your Bank Amount: "))

        s = Bank(Account_Number, Ifsc_code, Name,Father_name,Address)

        self.bank_client.append(s)

    def show_client(self):

        if len == 0:
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
    print("3. Exit")

    choice = input("Enter a chioce: ")

    if choice == "1":

        client.add_client()

    elif choice == "2":

        client.show_client()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid choice!")
