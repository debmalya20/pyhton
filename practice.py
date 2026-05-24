a= int(input("Enter a number="))
b= int(input("Enter b number="))
operator=input("Choose an operator\n('+' '-' '/' 'x''%')\nWnter your choice=")

match operator:
    case '+':
        print("The result=",a+b)
    case '-':
        print("The result=",a-b)
    case '/':
        print("The result=",a/b)


