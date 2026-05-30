# class factry_kolkata:
#     a="I am from kolkata"
#     def details(self):
#         print("I am kolkata factry worker")

# class factry_mumbai(factry_kolkata): # this is a inharitance
#     pass

# manager1=factry_mumbai()
# manager2=factry_mumbai()

# print(manager1.a)
# print(manager2.details())
# print(manager2.a)

# class name:
#     def __init__(self,name):
#         self.name= name
#     def shwo(self):
#         print(f"The name is {self.name}")

# class human(name):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age
#     def showage(self):
#         print(f"age of {self.name} is {self.age}")
       
# # human2=human("deb")
# human2=human("deb",20)
# human2.showage()

# class classroom:
#     def __init__(self,name):
#         self.name= name
#     def print(self):
#         print(f"The name of the student is {self.name}")

# class student(classroom):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age= age

#     def studentwithage(self):
#         print(f"The age of of {self.name} is {self.age}")
        

    
# student1=student("deb",20)
# student1.studentwithage()

class car:
    def __init__(self,bmw):
        self.bmw= bmw
    def show(self):
        print(f"The car is{self.bmw}")

class bike(car):
    def __init__(self,ducati,bmw):
        super().__init__(bmw)
        self.ducati= ducati
    def show(self):
        print(f"The car is {self.bmw} and the bike is{self.ducati}")

showroom=bike("panigalev4","bmw")
showroom.show()
        
    