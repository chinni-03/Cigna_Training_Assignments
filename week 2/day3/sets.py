s1 = set()
print(f's1: {s1}')

# ------------------
# TRUE and 1 clash (duplicates - True == 1, so only one will be considered (whichever comes first))
print('TRUE & 1'.center(30, '-'))

s2 = {1, 2, 3}
print(f's2: {s1}')

s3 = {True, 1, 2, 3}
print(f's3: {s3}')

# ----------------------
# ADD
print('ADD'.center(30, '-'))

s1.add(1)
s1.add(2)
s1.add(3)

print(f's1: {s1}')
print(f's1: {s1}')

# -----------------------
# REMOVE
print('REMOVE'.center(30, '-'))

s3.remove(2)        # returns None
print(f's3: {s3}')

# ------------------------
# UPDATE
print('UPDATE'.center(30, '-'))

s3.update([4, 5, 6, 7])
print(f's3: {s3}')

# ------------------------
# POP
print('POP'.center(30, '-'))

res = s3.pop()
print(f'res: {res}')

# -------------------------
# DISCARD
print('DISCARD'.center(30, '-'))

s3.discard(6)       # returns None
print(f's3: {s3}')

# -------------------------
# SE OPERATIONS
print('SET OPERATIONS'.center(30, '-'))

a = {1, 2, 3, 4, 5, 6}
b = {5, 6, 7, 8, 9, 10}

print(f'a union b: {a.union(b)}')       # |
print(f'a intersection b: {a.intersection(b)}')     # &
print(f'a difference b: {a.difference(b)}')     # -
print(f'b difference a: {b.difference(a)}')
print(f'a symmetric_difference b: {a.symmetric_difference(b)}')       # ^

# -------------------------
# FROZEN SET
# immutable unlike set (mutable)
fs = frozenset([1, 2, 3, 5, 6])
print(f'fs: {fs}')