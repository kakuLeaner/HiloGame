
# Kakungulu, P
# November 10, 2020
# HiLoGame 
# introduce game 
print('You will give the program the max number then you will guess the number')
print('*'*50 + '\n')
print('Give a maximum number then guess my number')
print('*'*50 + '\n')
import random
choiceMade = "y"
while choiceMade.lower() == 'y':
    # Ask user for Max number
    maxNum = int(input('What should the maximum number for this game be? '))
    print('\n')
    # computer guess
    randomNum = random.randint(1, maxNum)
    guessNum = int(input('Guess my number: '))
    # user guesses wrong
    while guessNum != randomNum:
        
        if guessNum < randomNum:
            print('Your guess is too low.')
            print('\n')
        if guessNum > randomNum:
            print('You guess is too high.')
            print('\n')
        guessNum = int(input('Guess my number: '))
    #if user guesses right
    if guessNum == randomNum:
        print('You guessed my number!')
        print('\n')
    # ask user to play again.
    choiceMade = input('Do you wish to play again?'' ''(Y/N): ')
    print('\n')
    #user ends playing
    choiceMade.lower() == 'n'
print('Thank you for playing!')
print(input('\n\nHit Enter to Close\n'))

    
