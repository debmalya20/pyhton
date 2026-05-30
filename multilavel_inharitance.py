class humans:
    def __init__(self,name):
        self.name= name
    
class animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class object(humans,animal):
    def __init__(self, name,age,):
        super().__init__(name)
    
    

call=object.show("rohit")
print(call)
