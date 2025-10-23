'''
MODULES
----------
library
act like packages
a file (.py)
consumer using import
'''

def greet(name):
    print(f'Greetings, {name}!')

sports = ['Cricket', 'Football', 'Hockey', 'Baseball', 'Handball']

scores = {
    'ODI': 8500,
    'Test': 8000,
    'T20': 200
}

class Employee:
    
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal

    def __str__(self):
        return f'Name: {self.name}\nSalary: {self.sal}'

if __name__ == "__main__":
    emp = Employee('harshini', 50000)
    print(emp)