from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def decorate(self):
        pass
   
class name(abstract):
    
    def name(self):
        print("The shop name=mistir dokan")
    def decorate(self):
        pass
class decorate(abstract):
    def name(self):
        pass
    def decorate(self):
        print("The decorate should have ac")

Name=name()
Name.name()