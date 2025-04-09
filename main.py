#number guessing game
import random 

print( "welcome to the number guessing game!")
print("guess a number beween 50 to 100")

number_to_guess = random.randrange(50,100)

chances =  5
guess_counter = 0

while guess_counter < chances:

    guess_counter += 1
    my_guess = int(input("please enter your guess: "))

    if my_guess ==number_to_guess:
        print(
            f"congratulations! you guessed the number {number_to_guess} in {guess_counter} attempts"
 )
        break

    elif guess_counter >= chances and my_guess != number_to_guess:
      print(f"Oops Sorry! the number is {number_to_guess} better luck next time")

    elif my_guess > number_to_guess:
        print("your guess is too high! try again")

    elif my_guess < number_to_guess:
        print("your guess is too low! try again")




