


##  Reference link ---  https://youtu.be/mrhccLHtyN4



# class Student:                                                                ###This is how to name a class ""
#         name="";                                                              ###"""The name and roll is just a variable,where i can use any anythigs as a variable
#         roll=0;                                                               ### and i can use it for any student as a data"""
#         def info(self):                                                       ###""""this is a methode , but it works like a function, and i can call it from anywhere,
#            print(f"My name is {self.name}, and Roll is {self.roll}")          ### info it's just a name of a function, but you have to use self as a paramiter"""

# a=Student()                                                                   ##"""there are some examples
# a.name="Hasan"
# a.roll=10
# a.info()


# b=Student()
# b.name="Rakib";
# b.roll=1
# b.info()

# c=Student()
# c.name="Muzahid"
# c.roll=2
# c.info()



######"""""""This is same like , i wrote above it. But it is just modified, if i want i can write anyway"""""



# class Student(object):
#     def __init__(self):
#         self.name=""
#         self.roll=0
#     def info(self):
#         print(f"My name is {self.name}, and Roll is {self.roll}")


# a=Student()          
# a.name="Hasan"
# a.roll=10
# a.info()


# b=Student()
# b.name="Rakib";
# b.roll=1
# b.info()

# c=Student()
# c.name="Muzahid"
# c.roll=2
# c.info()



######"""""""This is also same, but there is some paramiters in the methode/function"""""

# class Student(object):
#     def __init__(self,n):               ##There is n like a paramiter of this class
#         self.name=n
#     def info(self,r):
#         self.roll=r                    ##"""" r is like a paramiters 
#         tution_fees=4000               ##"""" This is a own variable of this function
#         print(f"My name is {self.name}, and Roll is {self.roll}.Class six tution fees is {tution_fees}TK per month")


# a=Student("Hasan")          
# a.info(10)


# b=Student("Rakib")
# b.info(1)

# c=Student("Muzahid")
# c.info(2)



######"""""""This is also same, but there is some paramiters in the methode/function"""""

class Student(object):
    def __init__(self,n,r):
        self.name=n
        self.roll=r
    def find_students_ability(self,s):
        sports=s
        if(self.roll <=5 and self.roll != 0):
            print(f"{self.name} is a good student, the roll is {self.roll} and favorite sports {sports}")
        elif(self.roll<=10 and self.roll >=6):
                   print(f"{self.name} is a avarage student, the roll is {self.roll} and favorite sports {sports}")
        else:
             print(f"{self.name} is a bad student, the roll is {self.roll} and favorite sports {sports}")
    def tution_fees(self,tf):
        self.tution_fees=tf
        print(f"{self.name} tution fees is {self.tution_fees}")


a=Student("Hasan", 10)
a.find_students_ability("football")
a.tution_fees(6000)

b=Student("Rakib", 1)
b.find_students_ability("Cricket")
b.tution_fees(5000)


b=Student("Muzahid", 2)
b.find_students_ability("football")
b.tution_fees(6500)