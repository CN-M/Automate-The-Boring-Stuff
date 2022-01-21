import pyperclip

a = 'a '
c = 'b '.upper()
e = 'c'
d = 'd'

#list = a, c, d, e

#f = ' Gay '.join(list)

string = ','.join(['cats','rats', 'bats'])
jane = 'John Jake Jason Ron Lake Rob'.split()
justified = 'Hello'.center(20,'=')
gym = 'Hey, you!'.replace('e','123')
pyperclip.copy('Heyyyyyy')

print(string)
print(jane)
print(gym)
print(pyperclip.paste())
