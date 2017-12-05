class Vehicle(object):

    vehicle_id = 0
    vehicles_sold = []

    def __init__(self,year,mileage,purchase_price,serial_number):

        self.__year = year
        self.__mileage = mileage
        self.__purchase_price = purchase_price
        self.__serial_number = serial_number

        if type(self.__year) != int or type(self.__mileage) != int or type(self.__purchase_price) != int:
            raise ValueError('The parameters for year, mileage and purchase_price have to be an integer!')

        self.__vehicle_id = self.generate_vehicle_id()
        Vehicle.vehicle_id += 1

    def __str__(self):

        return str(self.__vehicle_id)

    def get_id(self):
        "returns the instance's vehicle's id"

        return self.__vehicle_id

    @staticmethod
    def generate_vehicle_id():

        return Vehicle.vehicle_id + 100000

class Car(Vehicle):

    def __init__(self,year,mileage,purchase_price,serial_number,doors):

        super().__init__(year, mileage, purchase_price, serial_number)
        self.__doors = doors
        self.__wheels = 4


class Lorry(Vehicle):

    def __init__(self,year,mileage,purchase_price,serial_number,wheels,doors=2):

        super().__init__(year, mileage, purchase_price, serial_number)
        self.__doors = doors
        self.__wheels = wheels

        
class Motorcycle(Vehicle):

    classic_count = 0

    def __init__(self,year,mileage,purchase_price,serial_number,classic=False):

        super().__init__(year, mileage, purchase_price, serial_number)
        self.__classic = classic
        if classic:
            Motorcycle.classic_count += 1
    

### test cases ###

# initialising vehicle instances

Veh1 = Vehicle(2008,65000,7500,"34567851g4")
Veh2 = Car(2007,125000,5500,"e44653ftu1",4)
Veh3 = Car(2012,45000,8900,"gf5622iguz",doors=2)
Veh4 = Lorry(2005,180000,16000,"hbh997123f",6)
Veh5 = Lorry(2013,30000,35000,"hjbf17jbkh",8,4)
Veh6 = Motorcycle(1975,75500,40000,"bh545664rh",True)
veh_list = [Veh1,Veh2,Veh3,Veh4,Veh5,Veh6]


if __name__ == '__main__':
    for veh in veh_list:
        print(veh)
    
#prints     100000  
#           100001  
#           100002  
#           100003  
#           100004  
#           100005


# Veh7 = Motorcycle("year",10000,25000,"bjhgss4rdh",False)
# instance Veh7 generates an exception (ValueError) (uncomment to test)
