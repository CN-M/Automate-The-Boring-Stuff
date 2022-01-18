import numpy as np

def div42(x):
    try:
        return 42/x
    except ZeroDivisionError:
        print('Error: Tried to divide by zero')

print(div42(10))
print(div42(2))
print(div42(0))
print(div42(1))