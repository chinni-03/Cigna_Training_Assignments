li = [1, 2, 3, 4, 5]
print(li[-1])
print(f'li: {li}')

copied = li     # same address (shallow copy)

li2 = li.copy()     # different addresses (deep copy)
print(f'li2: {li2}')

li.append(6)
print(f'li after append: {li}')
print(f'li2 before append: {li2}')
li2.append(6)
print(f'li2 after append: {li2}')

# -----------------------
l7 = [1, 2, [3, 4, 5], 6]
l8 = l7.copy()
print(f'l7 before: {l7}')
print(f'l8 before: {l8}')
l8[2].extend([6, 7, 8])
print(f'l7 after: {l7}')
print(f'l8 after: {l8}')

# -----------------------
from copy import deepcopy

l7 = [1, 2, [3, 4, 5], 6]
l8 = deepcopy(l7)
print(f'l7 before: {l7}')
print(f'l8 before: {l8}')
l8[2].extend([6, 7, 8])
print(f'l7 after: {l7}')
print(f'l8 after: {l8}')

# -----------------------
# SORTED
a = [3, 1, 6, 4, 6, 2, 9, 10]
print(f'Sorted: {sorted(a)}')
print(f'Sorted reverse: {sorted(a, reverse=True)}')
print(f'a: {a}')
print(f'Sort: {a.sort()}')
print(f'a: {a}')
print(f'Sort reverse: {a.sort(reverse=True)}')
print(f'a: {a}')
