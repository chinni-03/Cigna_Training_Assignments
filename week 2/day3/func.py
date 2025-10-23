# calling a function
# def greet():
#     print('Greetings, Mr. Sachin!')

# greet()

# ------------------
# params for reusability
def greet(name):
    print(f'Greetings, {name}!')

greet('Harshini')

# default args must follow non-default args
def city_guest(name, city='New York'):      # default argument when args not passed
    print(f'Greetings, {name} from {city}!')

city_guest('Franck', 'Connecticut')
city_guest('Raghu')

# -----------------------
def product(x, y):
    return x * y

print(f'2 * 3 = {product(2, 3)}')

# -----------------------
# variable number of args (tuple)
print('variable args (tuple)'.center(30, '-'))

def product_all(*nums):
    print(nums)
    prod = 1
    for num in nums:
        prod *= num
    return prod

print(f'product of numbers [1, 2, 3, 4, 5]: {product_all(1, 2, 3, 4, 5)}')

# -----------------------
print('variable args (dict)'.center(30, '-'))

def extract_details(**details):
    print(details)
    for key, value in details.items():
        print(f'{key} => {value}')

extract_details(name='Sachin', age=50, runs=120)

# -------------------------
print('multiple returns'.center(30, '-'))

def calc(x, y):
    return x + y, x - y, x * y, x // y

print(f'result: {calc(1, 2)}')

# -----------------------
# doc strings
print('doc string'.center(30, '-'))

def sample():
    'this is a doc string'
    print('hi there!')

print(sample.__doc__)

# ----------------------
# example: doc strings
def adder(x, y):
    '''
    function adder(x, y):
    ---------------------
    1. if x and y are integers, then it will return the sum of x and y
    2. if x and y are strings, then it will return the concatenation of x and y
    3. if x and y are of different data types, it will throw an error
    '''
    return x + y

print(f'adder int: {adder(2, 3)}')
# print(f'adder strings: {adder('hi', 'harshini')}')      doesn't work due to the precedence issues of ' and "
print(f"adder strings: {adder('hi', 'harshini')}")
# print(f'adder int: {adder(2, 'hi')}')

# --------------------------
# named tuple
from collections import namedtuple

print('named tuple'.center(30, '-'))

def calc2(x, y):
    sum, diff, prod, quo = x + y, x - y, x * y, x // y
    res = namedtuple('results', 'sum diff prod quo')
    result = res(sum=sum, diff=diff, prod=prod, quo=quo)
    return result

print(f'namedtuple: {calc2(1, 2)}')

# -----------------------
# using modules.py
print(f'modules usage'.center(30, '-'))
from modules import Employee

emp = Employee('harshini', 5000)
print(emp)