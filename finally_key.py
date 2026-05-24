l=[1,4,3,2,7]
count=0

while count<3:
    try:
        index=int(input("Enter yoru index"))
        print(l[index])
        break
    except:
        count+=1
        print("Wrong input")

    finally:
        print("Its over")