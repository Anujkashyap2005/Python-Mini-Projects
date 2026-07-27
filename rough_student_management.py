import os


class Student:

    def __init__(self, roll_no, name, class_no, marks, attendance, fees):
        self.roll_no = roll_no
        self.name = name
        self.class_no = class_no
        self.marks = marks
        self.attendance = attendance
        self.fees = fees

    def grade(self):

        if self.marks >= 90:
            return "A+"
        elif self.marks >= 75:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "Fail"

    def room(self):

        if self.roll_no <= 25:
            return 101
        elif self.roll_no <= 50:
            return 102
        elif self.roll_no <= 75:
            return 103
        else:
            return 104

    def display(self):

        print("\n-----------------------------")
        print("Roll No      :", self.roll_no)
        print("Name         :", self.name)
        print("Class        :", self.class_no)
        print("Marks        :", self.marks)
        print("Attendance   :", self.attendance, "%")
        print("Fees Status  :", self.fees)
        print("Grade        :", self.grade())
        print("Class Room   :", self.room())
        print("-----------------------------")

class School:

    def __init__(self):
        self.students = []

    def add_student(self):

        roll = int(input("Enter Roll Number : "))
        name = input("Enter Name : ")
        cls = int(input("Enter Class : "))
        marks = float(input("Enter Marks : "))
        attendance = int(input("Enter Attendance % : "))
        fees = input("Fees Paid (Yes/No): ")

        s = Student(roll, name, cls, marks, attendance, fees)

        self.students.append(s)

        print("\nStudent Added Successfully.")

    def show_students(self):

        if len(self.students) == 0:
            print("\nNo Student Found")
            return

        for student in self.students:
            student.display()

school = School()

while True:

    print("\n====== STUDENT MANAGEMENT ======")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        school.add_student()

    elif choice == "2":
        school.show_students()

    elif choice == "3":
        print("Thank You")
        break

    else:
        print("Invalid Choice")