# FOR LOOP
print('FOR LOOP'.center(40, '-'))
for i in range(1, 11):
    print(i, end=" ")

print('\n')

for i in range(20):
    if i % 2 == 0:
        print(i, end = " ")
    else:
        continue

print('\n')

# WHILE LOOP
print('WHILE LOOP'.center(40, '-'))
i = 0
while i <= 10:
    print(i, end = " ")
    i += 1