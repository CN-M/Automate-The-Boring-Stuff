print('My name is:')
for i in range(105, 10, -2):
    print('Jimmy five times ' + str(i))
    if i == 77:
        print('Found it!')
        break

print('')

total = 0
for num in range(101):
    total = total + num
print(total)

print("")

z = 0
print('My name is:')
while z < 20:
    print('Jimmy Five times: ' + str(z))
    z += 5
    if z == 15:
        print('Found!')
        continue