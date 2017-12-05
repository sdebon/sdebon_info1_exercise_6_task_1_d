from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):

        self.name = name

        self.modules = []
        self.grades = {}

    def add_module(self,module):
        "appends a module to the instance list of modules and to the dictionary of grades as a key"

        self.modules.append(module.title)

        self.grades[module.title] = module.get_grade()

    def get_list_modules(self):
        "iterates over the list of modules and prints them one after another"

        for module in self.modules:
            print(module)

    def get_grades(self):
        "iterates over the dictionary of grades and prints the modules with the corresponding grades"

        for module in self.grades.keys():
            print('{0:s}: {1:d}'.format(module, int(self.grades[module])))

### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
