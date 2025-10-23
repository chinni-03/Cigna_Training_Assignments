a, b = 0, 1
n = int(input('Enter a number: '))
if n == 1:
    print(a)
elif n == 2:
    print(a, b)
else:
    print(a, b, end=' ')
    for _ in range(n - 2):
        print(a + b, end =' ')
        a, b = b, a + b
