import random

def getAnswer(number):
    if number == 1:
        return 'Yes'
    elif number == 2:
        return 'Maybe'
    elif number == 3:
        return 'No'


input('Ask a question: ')
print(getAnswer(random.randint(1, 3)))
