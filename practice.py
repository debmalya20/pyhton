# a= int(input("Enter a number="))
# b= int(input("Enter b number="))
# operator=input("Choose an operator\n('+' '-' '/' 'x''%')\nWnter your choice=")

# match operator:
#     case '+':
#         print("The result=",a+b)
#     case '-':
#         print("The result=",a-b)
#     case '/':
#         print("The result=",a/b)

#making my own decotater with muliples intpus as veriables:

# def inputs(*args):
#     #input=a,b,c,d
#     data= {}
#     for i in args:
#         value = input(f"Enter the value of {i} ")
#         data[i]=value
        
#     for i in args:
#         print(f"{i}={data[i]}")

# inputs("A","B","C","D")
def decorate(function):
    def wrapper(*args):
        print("This is the practice question if taking inputs using args\n")
        function(*args)
        print("\nThis action has ended")
    return wrapper

@decorate
def taking_input(*args):
    data={}

    for i in args:
        value=input(f"Enter the value of {i}=")
        data[i]=value

    for i in args:
        print(f"{i}={data[i]}")

taking_input("A","B","C","D")