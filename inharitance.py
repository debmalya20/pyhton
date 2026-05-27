class factry_kolkata:
    a="I am from kolkata"
    def details(self):
        print("I am kolkata factry worker")

class factry_mumbai(factry_kolkata): # this is a inharitance
    pass

manager1=factry_mumbai()
manager2=factry_mumbai()

print(manager1.a)
print(manager2.details())
print(manager2.a)