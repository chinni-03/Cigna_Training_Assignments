import csv
from prettytable import PrettyTable

# -------------------- READ ----------------------
# with open('C:\\Users\\C9K4H3\\Desktop\\training\\week 2\\data.csv', 'r') as FILE:
#     emp_details = csv.reader(FILE)
#     # col_name = next(emp_details)
#     # print(*col_name)        # * unpacks the data and removes the brackets and commas

#     # for row in emp_details:
#     #     print(*row)

#     pretty_table = PrettyTable(next(emp_details))       # prettytable object
#     for row in emp_details:
#         pretty_table.add_row(row)

# print(pretty_table)

# -------------------- WRITE ----------------------
data = [
    ['501', 'Jack', '28', 'HR', '65000'],
    ['235', 'Jill', '34', 'FIN', '35000'],
    ['150', 'John', '26', 'AC', '25000'],
    ['325', 'Jai', '21', 'DEV', '55000'],
    ['450', 'Guru', '38', 'DEV', '85000'],
    ['182', 'Sita', '32', 'PRC', '75000'],
    ['297', 'Gita', '36', 'SUP', '60000']
]

col_names = ['empid', 'empname', 'age', 'dept', 'salary']

with open('emp.csv', 'w', newline='') as WRITER:
    writer = csv.writer(WRITER)
    writer.writerow(col_names)
    for row in data:
        writer.writerow(row)

WRITER.close()