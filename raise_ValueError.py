try:
    a=input("Enter your name=")
    if a.isalpha():
     print("Your name is=",a)
    else:
        raise ValueError
except:
    print("You have entered a wrong input, please try again")
    