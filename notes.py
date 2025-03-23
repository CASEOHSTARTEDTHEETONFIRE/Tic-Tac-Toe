#import random

#random_number = random.randint(1, 5)
#print(random_number)

# Create a guess the number game that asks the user to guess a number between 1 - 100
# If the user guesses the number correctly, print "You win!"
# If the user guesses the number incorrectly, print ""Higher" if the number you guess is low than the random number
# If the user guesses the number incorrectly, print "Lower" if the number you guess is higher than the random number
# If the user guesses the number incorrectly, print "You lose" if the user guesses the number incorrectly 5 times. 
points= 5
questions=5
import random 
random_number = random.randint(1,1000)
while True:
    answer= int(input("guess the number from 1-1000 you have 5 tries."))
    if answer == random_number:
        print("You Win!")
        break
    questions = 0
    if answer < random_number:
        print("womp womp. Guess higher.")
        points -= 1
        questions -= 1
    if answer > random_number:
        print("womp womp. Guess lower.")
        points -= 1
        questions -=1

    if points <= 0: 
        print("you lose womp womp. ")
        print("The correct answer was " + str(random_number))
        break
    