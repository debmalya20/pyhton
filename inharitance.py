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

class name:
    def __init__(self,name):
        self.name= name
    def shwo(self):
        print(f"The name is {self.name}")

class human(name):
    pass
human1=human("deb")
human1.shwo()