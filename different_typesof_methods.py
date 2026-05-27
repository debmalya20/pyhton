class animal:
    name="lion" # this is a class attribute


#WHEN WE CREATE A FUNCTION IN SIDE A CLASS ITS KNOWN AS METHOD

    def __init__(self,age):#this function is known as instance method
        self.age=age
        #instance variable
        
        
    def show(self):
        print(f"The age of the animal is {self.age} ")
        
    @classmethod
    def hello(cls):
        print("hii") #we can take acess of all in main class

    @staticmethod
    def static():
        print("Heloow")

obj=animal(12)
obj.show()
