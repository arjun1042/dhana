#Durga Soft solution classes.


#class
class Student:
   
    ''' below are called functions in procedural languange'''
    '''below are methods in oops'''
     
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def details(self):
        print("----------------")
        print("Hello i am ", self.name)
        print("My Roll Number is ", self.rollno)
        print("my marks are ", self.marks)

#object
s1=Student("Bhuvana", 32, 89)
print(s1.name)
s1.details()
s2=Student("Dhana", 32,44)
s2.details()
print(s2.name)
print(s1.name)

#self is not keyword
#self is used in place of welf but self is not a keyword so costructor and method are require first arguemnt
#we use any name in place of self ex: welf, kelf, sefr...........

"""
Self:
--------

	1. Self is a reference variable, which is always pointing to current object. Within the python class, to access current object, we can use self.
	2. The first argument to the constructor is always self.
	3. The first argument to the method is always self
	4. We can use self always within the class only.
	Inside constructor, we can use self to declare object related variables(instance variables)
	5. Self is not a keyword, we can use any name like delf/kelf/ etc.,
	But it is recommended to use self.

	"""
