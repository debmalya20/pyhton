def details(**kargs):
    print("Your information are:\n")
    for i in kargs:
        print(f"{i}= {kargs[i]}")
       
details(name="Debmalya",age=20,skill="C,java,python")