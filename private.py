#This how you wontbe able to print the private class atributes
# class factry:
#     __a="kolkata"

#     def kolktafactry(self):
#         print("This is kolkata factry")

# class factry1(factry):
#     def show(self):
#         print(super().a)

# obj=factry1()
# obj.show()

#this is how you will be able to print the private attributes
# class factry:
#     __a="Kolkata"
#     def show(self): #we can beable to print cz we are acessing the prive attribute 
#         #inide the same fnction
#         print(factry.__a)

# obj=factry()
# obj.show()
class student:
    def __init__(self):
        self.name="deb"
        self._age=20 #protected
        self.__skill="Python" #private

    def show(self):
        print("The name of the student is",self.name)
        print("The age of the student is",self._age)
        print("The skill of the student is",self.__skill)
obj=student()
obj.show()