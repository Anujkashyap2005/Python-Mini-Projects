import sys
import random

def aky():
    
    print("===WELCOME IN===\n=== DHADHEECH MEMEORIAL PUBLIC SCHOOL===")
   

aky()

c = 0
r = 0

class Student():

  def __init__(self,name,clas,address):
      self.name = name
      self.clas = clas
      self.address = address

  def display(self):
      print(f"{self.name}")
      print(f"{self.clas}")
      print(f"{self.address}")

class School(Student):
    def __init__(self):
        self.Students = []

    def add_student(self,student):
        self.Students.append(Student)

    def show_student(self):
        for s in self.Students:
            s.display()


while True :
    print("\n ===School Exam List===")
    print("1. Class")
    print("2. Roll_Number")
    print("3. Exit")

    choice = input("Select a option:  ")
    aky()
    if choice == "1":
        # c = int(input("Enter Your class: "))
       
       
        if random.randint(1,10):
            print(f"Your Class is {random.randint(1,10)}")
        else:
            print("Sorry your class is not find out")

    elif choice == "2":
        r = int(input("Enter your roll number: "))
        if r >= 1 and r <= 25:
            print("Your room number is: 102")
        elif r >= 26 and r <= 50:
            print("Your room number is: 106")
        elif r >= 51 and r <= 75:
            print("your room number is : 108")
        elif r >= 76 and r <= 100:
            print("Your room number is : 115")
            
    elif choice == "3":
        print("Thanks for usig the school tools")
        break
    else:
        print("Sorry! I am not finded your class and roll_number ")

    


    

            

# roll_no = int(input("Enter your roll no: "))

# if roll_no >= 1 and roll_no <= 10:
#     print(f"Your room no is: 101 ")

# # n = int(input("Enter the room no.: "))
# # roll_no = int(input("Enter your roll no: "))

# elif roll_no >= 11 and roll_no <= 34:
#     print(f"Enter your room no is: 102")

# elif roll_no >= 35 and roll_no <= 55:
#     print(f"Your room no is: 103")

