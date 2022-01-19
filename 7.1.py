myCat = {'size': 'fat',
        'colour': 'red',
        'disposition': 'grumpy'}

x = myCat['size']


#print('My cat has ' + myCat['colour'] + ' fur.')
#print(x)

jack = {1245: 'Password', 42: 'Answer set'}

y = jack[1245]

eggs = {'Name': 'Kai', 'Age': 27, 'Hair Colour': 'Brown'}
ham = {'Age':27, 'Hair Colour': 'Brown', 'Age': 27, 'Name':'Kai'}

ham.setdefault("Age", 19)

z = eggs.get('Orientation', 'Unavailable')

a = list(eggs.keys())
b = list(eggs.values())
c = list(eggs.items())


for k, v in eggs.items():
    print(k + ':',v)

#print(a)
#print(b)
#print(c)
print(z)
print(ham)

#print(y)