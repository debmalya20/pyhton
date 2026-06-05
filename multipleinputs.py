#*args
#suppose i created a function of 2 peremeters and i want to add more the 2 parameters. The  we use *args

# def addition(a,b):
#     print(a+b)
# addition(12,45)

#now if i want more then 2 veriables
#When we create a *args it cretas a tupple 
def addition(function):
    def wrapper(*args):
        print("The sum of your inputs are:-")
        function(*args)
        print("Theis action is over")
    return wrapper
@addition
def addition(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)



addition(12,45,766,34.33)



    