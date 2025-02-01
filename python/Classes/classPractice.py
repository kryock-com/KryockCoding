import random

# a random number to be guessed
#using the ASCII chart and some other built-in function 
answer = (random.randint(97,122))

#  function that checks a guess
#passing in 1 paramater and that parameter is guess
def check_guess(guess):
    #converting guess to an ascii value
    guess = ord(guess)
    #check to see if to low
    if (guess < answer):
        print("You guessed too low")
        return False
    #check to see if to high
    elif (guess > answer):
        print("You guessed too high")
    #check to see is just right
    else:
        print("You guessed right!")
    
# the input prompts to begin the game
guess = input("You have three tries. Guess a letter between a and z: ").lower()
check_guess(guess)

guess = input("Guess again: ").lower()
check_guess(guess)

guess = input("Guess again: ").lower()
check_guess(guess)

print("Did you win?",chr(answer))




print(random.randint(1,1000))











