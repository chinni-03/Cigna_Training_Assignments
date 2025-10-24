'''
load - reads a JSON file
loads - convert JSon file to python dictionary
'''

import json

# -------------------- READ ----------------------
# JSON_FILE_READER = open('books.json', 'r')
# json_file = json.load(JSON_FILE_READER)

# # print(json_file)

# for book in json_file['books']:
#     print(book['name'])
#     print('-' * len(book['name']))
#     for key, value in book.items():
#         print(f'{key} => {value}')
#     print('-' * 30)

# JSON_FILE_READER.close()

# -------------------------
# LOADS
# data enclosed in single quotes
# empdata = '{"id": "B001","name": "Begning Python", "language": "English", "edition": "oreilly", "author": "Jack"}'
# print(type(empdata))

# # convert string into dictionary
# res = json.loads(empdata)
# print(type(res))

# -------------------- WRITE ----------------------
'''
dump - used to write a python serialized ibject to a json formatted data
dumps - used to encode any python object into a json formatted string
'''

player = {
    'players':[
        {'id': 'P101', 'Name': 'Sachin Tendulkar', 'Matches': 585, 'runs': 28500, 'age': 38},
        {'id': 'P102', 'Name': 'Sourav Ganguly', 'Matches': 430, 'runs': 19400, 'age': 36},
        {'id': 'P103', 'Name': 'Rahul Dravid', 'Matches': 390, 'runs': 18500, 'age': 35},
        {'id': 'P104', 'Name': 'Virendra Sehwag', 'Matches': 410, 'runs': 23500, 'age': 34},
        {'id': 'P105', 'Name': 'VVS Laxman', 'Matches': 298, 'runs': 15500, 'age': 36},
        {'id': 'P106', 'Name': 'Virar Kholi', 'Matches': 450, 'runs': 23000, 'age': 38},
        {'id': 'P107', 'Name': 'Yuvraj Singh', 'Matches': 520, 'runs': 19400, 'age': 36},
        {'id': 'P108', 'Name': 'MS Dhoni', 'Matches': 460, 'runs': 18500, 'age': 35},
        {'id': 'P109', 'Name': 'Md Kaif', 'Matches': 345, 'runs': 12400, 'age': 34},
        {'id': 'P110', 'Name': 'Suresh Raina', 'Matches': 410, 'runs': 15500, 'age': 36},
    ]
}

# JSON_FILE_WRITER = open('indian-team.json', 'w')
# json.dump(player, JSON_FILE_WRITER, indent=4)
# JSON_FILE_WRITER.close()

# -----------------------------------------
# convert data into JSON string 
empdata =  {'id': 'P101', 'Name': 'Sachin Tendulkar', 'Matches': 585, 'runs': 28500, 'age': 38}
res = json.dumps(empdata)
print(f'res: {res}')