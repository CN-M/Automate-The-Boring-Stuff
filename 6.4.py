import copy

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12] 

i = [1,2,6,8,13.5,712, -1, -9, 3.14]

i.sort()
x = copy.deepcopy(i)

i.remove(712)
i.append('Hello')
i[0] = 'Hi'

print(i)
print(x)

