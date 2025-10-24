FILE = open('data.txt', 'rb')       # mandatory to view in rb to move up and down and not character-wise (for from-current seek)

print(f'file tell: {FILE.tell()}')      # current cursor position

pos = FILE.seek(350, 0)         # move cursor to a position from 0 (start), 1 (current), 2 (end)
print(f'position: {pos}')

pos = FILE.seek(280, 1)
print(f'position: {pos}')

pos = FILE.seek(-300, 1)
print(f'position: {pos}')

pos = FILE.seek(250, 2)
print(f'position: {pos}')

pos = FILE.seek(-300, 2)
print(f'position: {pos}')

# pos = FILE.seek(-10, 0)       throws error because the cusor cannot move beyond the start
# print(f'position: {pos}')
print(len(FILE.read()))
print(FILE.seek(0, 2))
