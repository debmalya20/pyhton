class animal:
    def __init__(self,name,age):
        self.name= name
        self.age=age

    #donder method(Dobble ended method)

    def __str__(self): #This is a donder mthod that will automatically print by printing the object name.
        return f"The name of the animal is {self.name}"
    
    def __add__(self, other):
        return f"The age of the animals are {self.age + other.age}"
    
obj=animal("Tiger",20)
obj2=animal("Eliphent",30)
print(obj)
print(obj+obj2)