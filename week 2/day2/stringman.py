# emulate C style
format = 'Welcome %s! What a %s player!'
print(format)
values = ('Sachin', 'great')
print(values)
print(format % values)

format = 'Your rating is %.3f, %s!'
print(format)
values = (4.95793, 'Sachin')
print(values)
print(format % values)

print('Welcome %s! What a %s player!' % ('Sachin', 'great'))

# ----------------------------
from string import Template

tmpl = Template('Welcome $name, what a $adj player')
# address where the variabel is created
print(tmpl)
print(tmpl.substitute(name = 'Sachin', adj = 'great'))

# ------------------------------
print('Welcome, {}! What an {} player!'.format('Sachin', 'amazing'))
print('Welcome, {0}! What an {1} player!'.format('Sachin', 'amazing'))
print('Welcome, {name}! What an {adj} player!'.format(name = 'Sachin', adj = 'amazing', cnty = 'India'))

# ------------------------------
# INTERPOLATION
from math import pi, e
print(f'The value of pi is: {pi}')
print(f'The value of Euler\'s constant is: {e}')

# -----------------------------
import math
mod = math.__name__
print(f'The {mod} module has the value of pi as {math.pi}')

# ------------------------------
# r -> raw_string, s -> string, a -> ascii converted string
print('{val!s} {val!r} {val!a}'.format(val='A'))
# 10 -> spaces to the left, f -> float, b -> binary
print('{num:10} {num:f} {num:b}'.format(num=1024))
# alignment
'''
Numbers are aligned to the right side of spaces, while the strings are aligned to the left of the space
'''
print('{num:15} Tendular'.format(num='Sachin'))

print('{num:<15} Tendulkar'.format(num='Sachin'))      # left
print('{num:^15} Tendulkar'.format(num='Sachin'))      # center
print('{num:>15} Tendulkar'.format(num='Sachin'))      # right
# text in center (^) and fill with '-' out of (60 - len(num)) spaces
print('{num:-^60} Tendulkar'.format(num='Sachin'))
# pulls only first 6 characters
print('{:.6}'.format('Sachin Tendulkar'))
# 10 spaces reserved and 2 numbers printed excluding the decimal (.)
print('{pi:10.2}'.format(pi=pi))
print('One Google is {:,}'.format(10 ** 100))
# out of 10 spaces, get values and fill it with 0 (only 0s)
print('{pi:010.2}'.format(pi=pi))
print('{pi:010.2f}'.format(pi=pi))