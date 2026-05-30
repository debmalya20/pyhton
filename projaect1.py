#small project of factry using multilevel inharitance

class factry:
    def __init__(self,material):
        self.material= material
    
class kolkata_factry(factry):
    def __init__(self, material,color):
        super().__init__(material)
        self.color=color
class bagnan_factry(kolkata_factry):
    def __init__(self, material, color,cars):
        super().__init__(material, color)
        self.cars=cars

place=bagnan_factry(10,"red",20)
print("Materials=",place.material)
print("color=",place.color)
print("Crs=",place.cars)
        