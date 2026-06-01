class factry:
    a="kolkata"
    def show(self):
        print("This is kolkata")

class bagnan(factry):
    def show2(self):
        print(super().a)

obj=bagnan()
obj.show2()