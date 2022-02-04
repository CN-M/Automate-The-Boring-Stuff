#A Rock, Paper, Scissors game
import random, time

#Step 1: Output and explaining the game to the user

print("Hello, there! What's your name?")
name = input('Name: ')
print("Hello, " + name + ". We're about to play a game of rock paper scissors!")
print('You can pick from these 3 moves:')
print('Rock, Paper, or Scissors.')
print('')
print("We'll begin immediately! What's your move?")


playMove = input() #Player's move
playMove = playMove.lower()
compMove = random.randint(1, 3) #Computer's move

#Delay
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1!')
time.sleep(1)

print('')

#if compMove == 1:
 #   print('Rock!')
#elif compMove == 2:
 #   print('Paper!')
#elif compMove == 3:
 #   print('Scissors!')

print('')

#If it's a TIE
if playMove == 'rock' and compMove == 1:
     print("It's a tie! You both picked " + playMove + ".")
elif playMove == 'paper' and compMove == 2:
    print("It's a tie! You both picked " + playMove + ".")
elif playMove == 'scissors' and compMove == 3:
    print("It's a tie! You both picked " + playMove + ".")
#If it's a WIN
elif playMove == 'paper' and compMove == 1:
    print("Congratulations! You won! The computer picked:")
    print('Rock!')
elif playMove == 'rock' and compMove == 3:
    print("Congratulations! You won! The computer picked:")
    print('Scissors!')
elif playMove == 'scissors' and compMove == 2:
    print("Congratulations! You won! The computer picked:")
    print('Paper!')
#If it's a LOSS
elif playMove == 'scissors' and compMove == 1:
    print("what a shame! You lost! The computer picked:")
    print('Rock!')
elif playMove == 'rock' and compMove == 2:
    print("what a shame! You lost! The computer picked:")
    print('Paper!')
elif playMove == 'paper' and compMove == 3:
    print("what a shame! You lost! The computer picked:")
    print('Scissors!')
else:
    print('Looks like you made an incorrect input. Restart the programm and try again.')