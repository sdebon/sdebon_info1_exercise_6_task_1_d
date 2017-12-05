from vehicle import *

import random


class Customer(object):
    
    def __init__(self,name):

        self.__name = name
        self.__score = self.credit_score()

    def __str__(self):

        return "Customer: {0:s}".format(self.__name)

    def credit_score(self):
        "gives a boolean to the instance variable; if greater than 60 True otherwise False"
        num = random.randint(0,100)
        if num > 60:
            return True
        else:
            return False

    def get_score(self):
        "returns the instance's score (boolean-type)"
        return self.__score


class VIP_Customer(Customer):

    def credit_score(self):
        "always returns True"
        return True


### test cases ###

# initialising customer instances

Wendy = Customer("Wendy")
Heidi = VIP_Customer("Heidi")

if __name__ == '__main__':
    print(Wendy) # expected output: Customer: Wendy
    print(Heidi) # expected output: Customer: Heidi

    print(Wendy.get_score()) # expected output: True or False depending on random score
    print(Heidi.get_score()) # expected output: True