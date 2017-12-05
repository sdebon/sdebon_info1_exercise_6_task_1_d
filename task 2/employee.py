from vehicle import *
from customer import *

class Employee(object):

    emp_id = 0

    def __init__(self, name):

        self.__name = name
        self.__id = Employee.emp_id
        Employee.emp_id += 1

    def __str__(self):

        return 'Employee: {0:s} is of type {1:s}'.format(self.get_name(), self.get_title())

    def get_name(self):

        return self.__name
    
    def get_title(self):

        return 'Subordinate'
    
class Manager(Employee):

    def get_title(self):

        return 'Manager'

    def get_sales_report(self,salesman):

        if not salesman.get_name() in Salesman.sales:
            raise KeyError

        print(Salesman.sales[salesman.get_name()])

class Salesman(Employee):

    sales = {}

    def sale(self,vehicle,sales_price,customer):
        if customer.get_score():
            Salesman.sales[self.get_name()] = Salesman.sales.get(self.get_name(), 0) + sales_price
        else:
            print('Error: The customer does not have enough credit score')


### test cases ###

## initialising employee instances

Eric = Manager("Eric")
Kyle = Employee("Kyle")
Stan = Salesman("Stan")
Kenny = Salesman("Kenny")
Craig = Salesman("Craig")

## printing employee instances

print(Eric) # expected output: Employee: Eric is of type Manager
print(Kyle) # expected output: Employee: Kyle is of type Subordinate
print(Stan) # expected output: Employee: Stan is of type Subordinate
print(Kenny) # expected output: Employee: Kenny is of type Subordinate
print(Craig) # expected output: Employee: Craig is of type Subordinate


## registering sales

Kenny.sale(Veh2,6000,Heidi)

Stan.sale(Veh1,9000,Wendy)


## printing an individual sales report:

Eric.get_sales_report(Kenny)
# expected output:
# Kenny's current cumulative sales:
# 6000