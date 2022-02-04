#A Guess the number game
import random

name = input("Yo, what's your name, kid? ")
print('Nice to meet you, ' + name + '.')

print("I'm thinking of a number betweem 1 and up to" + \
     " and including 20. You have 6 guesses. I will give you hints. Shoot!")

sec_num = random.randint(1, 21) # Secret Number



for i in range(1,7):
    print("What's your guess?: ")
    print("")
    guess = int(input())
    if guess < sec_num:
        print("Your guess is too low")
    elif guess > sec_num:
        print('Your guess is too high')
    else:
        break

if guess == sec_num:
    print("Well done! You got it right in " + str(i) + ' guesses')
else:
    print("You ran out of guesses. The number I was thinking of was " + str(sec_num))