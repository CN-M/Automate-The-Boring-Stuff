#This program says Hello, asks for your name, prints the number of characters in your name, asks for your age, and then tells you how old you'll be in a year from now

print('Hello!')
print("What's your name?")
name = input()

print('Nice to meet you, ' + name + "! I hope we'll have a swell time learning Python together!")
print('Your name is ' + str(len(name)) + " letters long!")
print("What's your age?")
age = input()

print("Nice! You'll be " + str(float(age) + 1) + " in a year from now." )