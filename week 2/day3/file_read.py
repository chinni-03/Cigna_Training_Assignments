'''
read mode - only read file (default)
'''
file = open('data.txt', 'r')

# reads whole doc
# st = file.read()
# print(st)

# reads one line at a time
# line1 = file.readline()

# reads all lines and stores it in a list (till \n)
# lines = file.readlines()
# print(lines)

# for line in file.readlines():
#     print(line)
#     print('*' * 20)

file.close()        # if file uses memory, it stays in the buffer

