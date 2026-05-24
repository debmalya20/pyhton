try:
    a=int(input("Enter a number="))
    print(f"The numti plication table of{a} is=")

    for i in range(1,11):
     print(f"{int(a)} x {i}={int (a)*(i)}")
except:
  print("Some error occered")

print("Done")

