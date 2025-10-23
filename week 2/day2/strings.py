print('maketrans'.center(40, '-'))
st = 'hello world'
print(f'st: {st}')

# a and b should be of same length
a = 'helowrd'
b = a.upper()

# returns a dict containing ASCII values mapped as {old: new}
res_table = st.maketrans(a, b)

# translation using the generated table
res = st.translate(res_table)
print(f'translated: {res}')