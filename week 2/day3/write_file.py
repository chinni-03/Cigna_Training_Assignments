'''
writing into a file
-------------------
1. file already present => deletes the content of the file and rewrites it
2. file not present => creates a file and writes into it
3. file already present => add to the end of the file
'''

FILE = open('myfile.txt', 'w')

# single line
# data = input('enter the contents to be written into a file: ')
# FILE.write(data)

# multiple lines
# l1 = 'The first line~\n'
# l2 = 'The second line~\n'
# l3 = 'The third line~'
# FILE.writelines([l1, l2, l3])

# appending text
# FILE = open('myfile.txt', 'a')
# data = input('enter the contents to be written into a file: ')
# FILE.write(f'\n{data}')

FILE.close()