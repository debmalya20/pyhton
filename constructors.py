# class showroom:
#     def __init__(self,cars,tiers,breaks):
#         self.cars=cars
#         self.tiers=tiers
#         self.breaks=breaks
# dealer=showroom(20,80,80)
# print(dealer.cars)

class house:
    def __init__(self,room,tables,bed):
        self.room=room
        self.tables=tables
        self.bed=bed

    def requirements(self):
        print(f"rooms={self.room}")
        print(f"tables={self.tables}")
        print(f"bed={self.bed}")
        


shop=house(4,4,4)     
print(shop.requirements())





    




