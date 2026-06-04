class animal:
    @property 
    #if you use this property decorattor then we dont have tp us bracket while calling the method

    def sound(self):
        print("Hukka huaaaa")

obj=animal()
obj.sound