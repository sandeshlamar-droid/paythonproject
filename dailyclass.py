# 1. Create a Python program that prompts the user to enter their age. If the age is less
# than 18, print you are a minor. If the age is between 18 and 60, print you are an
# adult. For ages over 60, print you are a senior citizen. The program should continue
# until the user inputs stop.
import random
while True:
    age = int(input('enter your age:'))
    if age < 18:
        print('your are a minor')
    elif age > 18 and age < 60:
        print('you are a adult')
    elif age >= 60:
        print('you are senior citizen')
    user_input = input('do you want to continue:')
    if user_input == 'no':
        break


# 2. Write a Python program that simulates waiting for a specific vehicle, such as a bus.
# The program should repeatedly prompt the user to input the name of a vehicle. If the
# input is not bus, the program should print waiting and continue. Once the user inputs
# bus, the program should print finally the wait is over and terminate the loop.

while (vehicle := input('enter your vehicle name:')) != 'bus':
    print('waiting')
else:
    print('wait is over')


# 3. Generate a frequency table for the ratings list which is initialized below. Ratings =
# ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
#  a. Start by creating an empty dictionary named content_ratings
#  b. Loop through the ratings list. For each iteration, complete the following:
#  If the rating is already in content_ratings then increment the frequency of that rating
# by 1.
#  Else, initialize the rating with a value of 1 inside the content_ratings dictionary

Ratings = ['4+', '9+', '12+', '17+', '4+',
           '12+', '4+', '9+', '17+', '12+', '4+', '17+']


content_ratings = {}
i = 0
while i in range(len(Ratings)):
    content_ratings[Ratings[i]] = content_ratings.get(Ratings[i], 0)+1
    i += 1
print(content_ratings)

i = 0
while i < len(Ratings):
    content_ratings[Ratings[i]] = content_ratings.get(Ratings[i], 0)+1
    i += 1
print(content_ratings)


# 4. Write a Python program that generates a random number between 1 and 10 and
# prompts the user to guess the number. The program should provide hints such as
# guess higher or guess lower based on the user's input. Once the user guesses the
# correct number, the program should display the number of attempts it took to guess
# the correct number.

num1 = random.randrange(1, 10)

while True:
    number = int(input('Guess the number between 1 and 10: '))

    if number < num1:
        print("Guess higher")


# 5. Write a Python program that simulates a login system. The program should prompt
# the user to enter a username and password. If both are correct for example username
# is admin and password is 1234, print Login successful and exit. If either is incorrect,
# print Invalid credentials, try again. Allow the user up to 3 attempts before locking
# them out with the message too many failed attempts

user_name = input('Enter your username:')
password = input('Enter your password:')
attempts = 0
max_attempts = 3
if username == 'admin' and password == '1234':
    print('Login successful')

else:
    print('Please try again.')

if attempts == max_attempts:
    print('Too many failed attempts')


# 6. Write a Python program that simulates a basic arithmetic quiz. Generate two random
# numbers between 1 and 30 and ask the user to provide the result of their
# multiplication. If the answer is correct, print correct and generate a new question. If
# the answer is wrong, print Incorrect, try again. Allow the user to stop the quiz when
# the user enters exit.

while True:
    if generate:
        num1 = random.randrange(1, 30)
        num2 = random.randrange(1, 30)
        correct_answer = num1 * num2
        Generato = False

user_input = input(f"{num1}x{num2}?").strip()

if user_answer == correct_answer:
    print("correct")

else:
    print("Incorrect, please try again.")


if user_input == 'exit':
    print("Thanks for playing !")


# 7. Write a Python program that prompts the user to repeatedly enter a name. If the user
# enters the phrase good luck, the program keeps track of how many times the phrase
# has been entered. When the phrase has been entered three times, the program should
# display a message stating you typed good luck three times. For each entry of good
# luck before the third occurrence, display the message you typed the same word
# [count] times. Continue this process until the phrase has been entered three times.


# 8. Generate a random number (1–50). Give the user up to 7 attempts to guess it using a
# while loop. Track remaining attempts and stop early if they guess correctly or run out
# of tries


# 9. Write a Python program that simulates a basic elevator system. The program should
# keep track of the elevator's current position and allow a user to travel to different
# floors until they choose to exit.
# Requirements:
# a) Starting State: The elevator should start on floor 1.
# b) Continuous Loop: Use a while loop to repeatedly ask the user for a
# destination floor.
# c) Input Handling: If the user enters 0, the program should print a goodbye
# message and terminate. If the user enters something that isn't a number,
# handle the error gracefully so the program doesn't crash.
# d) Logic: If the target floor is higher than the current floor, print a ‘Going up’
# message. If the target floor is lower than the current floor, print a ‘Going
# down’ message. If the user is already on the requested floor, inform them
# of that.
# e) State Update: After moving, update the current floor to the target floor so
# the next movement starts from the new location.


# 10. Develop a two-player Rock, Paper, Scissors game. The program should automate the
# scoring logic and continue the match until one player reaches a specific score.
#  Tasks:
# 1. Setup:
# > Initialize two score trackers player1_score and player2_score starting at
# 0.
# 2. The Game Loop:
# > Use while loop to represent the ongoing match.
# > Inside the loop, prompt both Player 1 and Player 2 for their choices: rock,
# paper, or scissor.
# > Make ensure the inputs are case-insensitive.
# 3. Scoring Logic:
# > If both choices are the same, print ‘it’s a tie’.
# > If Player 1's choice beats Player 2's choice, if it does, increment Player 1's
# score.
# > After every round, print the current score.
# 4. Condition:
# > Implement a check to see if either player has reached 5 points.
# > If a player reaches 5, announce the winner example ‘player1 won the
# game’ and use the break statement to end the program.


# 11. Write a python program to get the following output using while loop.
# 1 – 49
# 2 – 48
# 3 – 47
# 4 – 46
# .
# .
# .
# 48 – 2
# 49 –1


# 12. Write a program that accepts a number from the user and calculates the sum of all
# numbers from 1 up to that number.


# 13. Print alphabet series A to Z.
# Output: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z


# 14. Write a program to find the numbers which are below 20 in a list.
# number = [2, 40, 21, 31, 10, 7, 5]
