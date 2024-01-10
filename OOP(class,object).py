class Student:
    def __init__(self):
        self.name = input("enter your name: ")
        self.rollno = int(input("enter roll number: "))
        self.marks = int(input("enter marks: "))

    def details(self):
        print("----------------")
        print("Hello i am ", self.name)
        print("My Roll Number is ", self.rollno)
        print("my marks are ", self.marks)

s=Student()
s.details()
