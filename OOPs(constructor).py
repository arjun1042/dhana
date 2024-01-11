# Constructor in python


'''
1. constructor is a special method
2. the name of the constructor is always __init__()
3. We are not required to call constructor explicitly.
   It will be executed automatically when we are creating
   an object
4. per object, constructor will be execute only once.
5. The main purpose of constructor is to declare and
   initialize instance variables

   __init__ means initialization

6. constructor should have atleast one argument i.e, self

7. default constructor will be executed which is provided by PVM

8. We can call constructor explicitly, then it will be executed
   just like a normal method and new object won't be created

9. Constructor/ Method overloading are not applicable
   If we are trying to declare multiple constructors, PVM will
   will always consider only last constructor

        
'''

'''
#example-1

class Test:
    def __init__(self):
        print("print Constructor execution.......")


t1= Test()
t2= Test()
t3= Test()
t4= Test()
t5= Test()

'''
#Example-2:
'''
class Student:
    def __init__(self, name, rollno, marks): #constructor
        self.name=name
        #print(name)
        self.rollno=rollno
        self.marks=marks

s1=Student("raju",102, 67)
#print(s1.name)

    '''

# default constructor

#7. default constructor will be executed which is provided by PVM

#example-3

'''
class Test:
    def m1(self):
        print('method execution........')

t=Test()#default constructor will be executed
t.m1()

'''

#example-8:
# 8. We can call constructor explicitly, then it will be executed
#    just like a normal method and new object won't be created

'''

class Test:
    def __init__(self):
        print("print Constructor execution.......")


t1= Test()
t1.__init__()
t1.__init__()

'''
#9. Constructor/ Method overloading are not applicable
#   If we are trying to declare multiple constructors, PVM will
#   will always consider only last constructor

# Example-9

'''

class Test:
    def __init__(self):
        print("print Constructor 1 execution.......")

    def __init__(self,x):
        print("print Constructor 2 execution.......")

t=Test(10)

'''

class Test:
    def __init__(self, name):
        self.name=name
class Demo:
    def __init__(self, name):
        self.name=name
t1=Test('arjun')
print(t1.name)
t2=Demo('raj')
print(t2.name)



# I/Q:- difference b/w constructor and method

'''
Method
-------

1. method name can be anything
2. methods won't be executed automatically
3. per object, we can call method any number of times.
4. inside method we ca write business logic based on our
   programming requirement

constructor
-----------
1. constructor name should be __init__()
2. constructor will be executed automatically, whenever we are
   creating an object.
3. per object, we can call only one time.
4. inside constructor we have to write code to declare and
   initialize instance variable.

   '''
