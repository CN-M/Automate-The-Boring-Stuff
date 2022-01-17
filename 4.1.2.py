
numcats = input("How many cats do you have?: ")

def cats():
    if int(numcats) >= 5:
            print('Many pussy')
    elif int(numcats) < 0 :
        print('Please enter a positive number')
    else:
        print('Not so many pussy')


while True:
    try:
        cats()
    except Exception as e:
        print(e)
        print('You did not enter a number, bitch')
        continue
    else:
        break
            

