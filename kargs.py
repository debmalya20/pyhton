# def details(**kargs):
#     print("Your information are:\n")
#     for i in kargs:
#         print(f"{i}= {kargs[i]}")
       
# details(name="Debmalya",age=20,skill="C,java,python")

def details(function):
    def wrapper(**kargs):
        print("This is the information about the clint\n")
        function(**kargs)
        print("\nEND TO END ENCRYPTED")
    return wrapper
@details
def details(**kargs):
    # print("The information about the clint\n")
    for i in kargs:
        print(f"{i}={kargs[i]}")

details(name="debmlaya", age=20, roll=2575017)