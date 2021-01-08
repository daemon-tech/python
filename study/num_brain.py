import random
import os
from time import sleep

def string_time_function():
    word = "Write the number: "
    for o in range(0, len(word)):
            print(word[o], end="")
            sleep(3)
    return word

def return_number():
    random_number = random.randrange(0, 9+1)
    number = 0
    for i in range(0, 7+1):
        if len(number) != 8:
            if number == 0:
                number = str(random_number)
            else:
                number += str(random_number)
        return number

def brain_game():
    game_loop_end = 10
    game_loop_start = 0
    for j in range(0, game_loop_end):
        game_loop_start += 1
        if game_loop_start < game_loop_end: # actual code
            ran_number = return_number() #saves the number in a variable, to check later if its the true value
            print("Remember: {}".format(ran_number))
            sleep(10)
            os.system("clear")
            sleep(1)
            print(string_time_function())
            userInput = input("= ")
            if userInput == ran_number:
                print("Correct: {} = {}".format(userInput, ran_number))
            else:
                print("Wrong, the righ answer is: {} , your input was: {}.".format(ran_number, userInput))
        else:
            print("Excercise finished!")

if __name__ == '__main__':
    brain_game()
