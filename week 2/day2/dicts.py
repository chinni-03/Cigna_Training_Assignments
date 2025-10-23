player = {
    'name': 'Sachin',
    'age': 50,
    'runs': 120,
    'opp': 'PK'
}

# for i, j in enumerate(player):
#     print(i, j)

print(player)

for x in player:
    print(f'{x} => {player[x]}')

# -----------------------------
# UPDATE
print('update'.center(30, '-'))
player['name'] = 'Sachin Tendulkar'
print(player)

player.update({'country': 'India'})
print(player)
player.update({'runs': 200})
print(player)

# -------------------------------
print('del'.center(30, '-'))
# DELETE
del player['opp']
print(player)

# -------------------------------------
print('keys and values'.center(30, '-'))
print(f'keys: {player.keys()}')
print(f'values: {player.values()}')

for i in player.keys():
    print(f'{i} => {player[i]}')

# ------------------------------------
print('items'.center(30, '-'))
for i, j in player.items():
    print(f'{i} => {j}')

# -----------------------------------
print('from keys'.center(30, '-'))
keys = ['BLR', 'NYC', 'ZUR', 'MUN']
res = dict.fromkeys(keys)
print(f'res: {res}')
res = dict.fromkeys(keys, 'Not defined')
print(f'res: {res}')

# -------------------------------------
# SET DEFAULT
print('set default'.center(30, '-'))
print(player)
player.setdefault('opp', 'AUS')
player.setdefault('name', 'Sachin')
print(player)

# -------------------------------------
# POP
# del doesn't return a value, but pop does
print('pop'.center(30, '-'))
res = player.pop('opp')
print(f'res: {res}')
print(f'player: {player}')

# -----------------------------------------
# POP ITEM
print('pop item'.center(30, '-'))
res = player.popitem()
print(f'res: {res}')
print(f'player: {player}')