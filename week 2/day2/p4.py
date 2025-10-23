count = 0
for i in range(151, 49, -1):
    if i % 2 == 0:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
        else:
            count += 1
print(f'Number of prime numbers: {count}')