from abc import ABC ,abstractmethod

class abstruct(ABC):
    @abstractmethod
    def aryea(self):
        pass
    @abstractmethod
    def cars(self):
        pass

class newshop(abstruct):
    def shop_name(self):
        pass

class aryes(abstruct):
    def aryea(self):
        print("I have created")
    def cars(self):
        pass
class cars(abstruct):
    def aryea(self):
        pass
    def cars(self):
        print("Cat is present")
        
        
        

obj=aryes()
obj.aryea()
obj=cars()
obj.cars()



