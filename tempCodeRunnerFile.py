class name:
    def __init__(self,name):
        self.name= name
    def shwo(self):
        print(f"The name is {self.name}")

class human(name):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def showage(self):
        print(f"age of {self.name} is {self.age}")
       
# human2=human("deb")
human2=human("deb",20)
human2.showage()
