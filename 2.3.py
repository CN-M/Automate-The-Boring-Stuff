x = 0

while x < 5:
    print('Hello World')
    x += 2
    print(x)

print('')

name = ''

while True:
    name = input('Please type in "your name": ')
    if name == 'your name':
        break
print('Thank you!')