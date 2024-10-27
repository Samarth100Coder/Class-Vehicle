class Vehicle:
    def __init__(self,speed,mileage):
        self.speed=speed
        self.mileage=mileage
        print('Mileage:',self.mileage)
        print('Speed:',self.speed)

v1=Vehicle(200,30)
v2=Vehicle(300,32)