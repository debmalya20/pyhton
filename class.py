print('''Hellow welcome to deb & barna stores.
How can we help you sir?''')

a="bike"
b="car"
c=input('''Enter your choice sir!
would you like to buy a car or a bike sir=''')
bike=["1 BMW","2 TVS","3 ROYEL ENFILD","4 HONDA"]

if c==a:
    
    for i in range(0,4):
        print(bike[i])

option=int(input("Enter your choice="))


match option:
    case 1:
         print(f"The price of{bike[0]} is= $1200-$2000")
    case 2:
         print(f"The price of{bike[1]} is= $600=$1000")
    case 3:
         print(f"The price of{bike[2]} is= $750-$1100")
    case 4:
        print(f"The price of{bike[3]} is= $1200-$2000")


    




