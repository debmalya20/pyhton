a=int(input("Enter a number="))
b=int(input("Enter a number="))
option=input("Enter an operator[-,+,/,%,x]")

c =a+b

match option:
    case '-':
        print("Result=",a-b)
    case '+':
        print("Result=",a+b)
    case '/':
        print("Result=",a/b)
    case '%':
        print("Result=",(c/100)*c)
    case 'x':
        print("Result=",a*b)
    case _:
        print("Invalid input")
