# 4. Design a program for a 'Student Resource Portal.' The program should ask for a username and a password.
# If the username is admin and password is ad123, print Access Granted: Faculty Dashboard.
# If the username is student and password is st2026, print Access Granted: Notes and Practice Questions.
# For any other combination, print Invalid Credentials. Please try again.
# ANS:
user_name = input("enter a username:")
password = input("enter a password:")

if user_name == 'admin' and password == 'ad123':
    print("access granted ! ")

elif user_name == 'student' and password == 'st2026':
    print("access granted ! ")

else:
    print("unknown invalid credentials ! ")


# 5. Design a Traffic Light System. Given a variable light that can be red, yellow, or green, print the correct instruction.
# Also handle an invalid color with an error message.
# ANS:
light = int(input('red : stop !', 'yellow : slow !', 'green : go !'))

if light == 'red':
    print('stop !')

elif light == 'yellow':
    print('slow !')

elif light == 'green':
    print('go !')

else:
    print('unknown invalid color !')

# 6. Write a match statement that takes a number 1–4 and prints the corresponding season: 1=spring, 2=summer, 3=autumn, 4=winter.
# Default: unknown.
# ANS:
season_number = int(input('enter a season number'))

if season_number == 1:
    print('spring')
elif season_number == 2:
    print('summer')
elif season_number == 3:
    print('autum')
elif season_number == 4:
    print('winter')

else:
    print('unknown number')


# 7. Design a Bank Loan Approval System. Approve a loan only if ALL three conditions are met: Age is between 21 and 60 (inclusive)
# Monthly income is at least 30,000 Credit score is at least 700 If not approved, print which condition failed.
# ANS:
Age = int(input('enter your age:'))
Income = int(input('enter your monthly income:'))
credit_score = int(input('enter your score:'))
age = int(input('Enter your age:'))

if 21 <= age <= 60:
    if Income >= 30000:
        if credit_score >= 700:
            print("Approved!")

        else:
            print("Not_approved ! Credit Score is less than 700")
    else:
        print("Not_approved ! Income is less than 30k")
else:
    print("Age is not between 21 and 60")


# 8. You are developing a simple ticket booking system for a movie theatre. The ticket price depends on the age of the person and
# whether they have a membership card. If the person is under 12, the ticket is free. If the person is between 12 and 60:
# If they have a membership card, the ticket costs Rs. 150. If not, the ticket costs Rs. 200. If the person is
# above 60, they get a senior citizen discount, and the ticket costs Rs.100. Write a Python program using nested
# if-else to calculate and print the ticket price based on the user's age and membership status.
# ANS:
Age = int('Enter you age: ')
membership = input('Do you have membership card? Yes or No: ').lower()
ticketCost = 200

if age < 12:
    print('Ticket is Free of Cost!')
    ticketCost = 0

elif 12 <= age <= 60 and membership != 'yes':
    print(f"Ticket Cost = {ticketCost}")

elif 12 <= age <= 60 and membership == 'yes':
    ticketCost = 150
    print(f"Ticket Cost = {ticketCost}")

else:
    ticketCost = 100
    print(f"You get a Senior citizen discount. Ticket Cost = {ticketCost}")


# 9. A company decided to give bonus of 5% to employee if his/her year of service is more than 5years.
#  Ask user for their salary and year of service and print the net bonus amount.
# ANS:
salary = int(input("Enter your salary: "))
service = float(input("Enter your year of service: "))

if service > 5:
    print(f"Net Bonus = {0.05 * salary}")

else:
    print("You don't have any bonus !")


# 10. Write a python program which accepts the radius of circle from user and compute the area.

radius = float(input("Enter the radius of a circle: "))

print(f"Area of circle = {3.14 * radius ** 2}")


# 11. Accept the age, gender ('M', 'F'), number of days and display the wages accordingly.
# ANS:
Age = int(input("Enter your age: "))
Gender = input("Enter your gender, M or F: ").capitalize()

if 30 > age >= 18:
    if Gender == 'M':
        print("Your wage per day is 700")

    elif Gender == 'F':
        print("Your wage per day is 750")

    else:
        print("Invalid gender!")

elif 40 >= age >= 30:
    if Gender == 'M':
        print("Your wage per day is 800")

    elif Gender == 'F':
        print("Your wage per day is 850")

    else:
        print("Invalid Age!")


# 12. Accept input from user
# If given number is a multiple of both 3 and 5 prints Fizz Buzz instead of number.
# If given number is a multiple of 3 but not 5 prints Fizz instead of number.
# If given number is a multiple of 5 but not 3 prints Buzz instead of number.
# If given number is not multiple of 3 or 5 prints value as usual.
# ANS:
Number = int(input("Enter a number: "))

if Number % 3 == 0:
    if Number % 5 == 0:
        print("Fizz Buzz")
    else:
        print("Fizz")

else:
    if Number % 5 == 0:
        print("Buzz")

    else:
        print(Number)


# 13. A utility company charges different rates based on electricity usage:
# If usage < 100 units then cost Rs 5 per unit
# If usage is between 100 to 300 units:
# First 100 units: Rs 5
# Next units: Rs 8
# If usage is > 300 units: First 100: Rs 5 Next 200: Rs 8 Remaining: Rs10
# ANS:
usage = float(input("Enter your electricity usage in units: "))

if usage < 100:
    print(f"Cost: Rs. {usage * 5}")

elif usage <= 300:
    print(f"Cost: Rs. {(100 * 5) + ((usage - 100) * 8)}")

elif usage > 300:
    print(f"Cost: Rs. {(100 * 5) + (200 * 8) + ((usage - 300) * 10)}")

# 14. Write a complete Python program that:
# Asks Player 1 to enter their move ( input: rock, paper, or scissors)
# Asks Player 2 to enter their move ( input: rock, paper, or scissors)
# Prints who wins or if it's a tie
# ANS:
player1 = input("player-1 enter your move (rock paper scissors):").lower()
player2 = input("player-2 enter your move (rock paper scissors):").lower()
action_list = ['rock', 'paper', 'scissors']
if player1 in action_list and player2 in action_list:
    if player1 == player2:
        print('draw')
    elif player1 == 'rock' and player2 == 'scissors':
        print('                 player_1 wins            ')
    elif player1 == 'scissors' and player2 == 'paper':
        print('                 player_1 wins            ')
    elif player1 == 'paper' and player2 == 'rock':
        print('                 player_1 wins            ')
    else:
        print('                 player_2 wins            ')
else:
    print('invalid choice')


# 15. Write a Python program that takes a number as input, first checks if it is positive
#  if yes then check whether it is even or odd.
# ANS:
num = int(input("Enter a number: "))

if num >= 0:
    if num % 2 == 0:
        print(f"{num} is positive and even")

    else:
        print(f"{num} is positive and odd")

else:
    print(f"{num} is negative")


# 16. A store gives a 20% discount if the total purchase is above RS1000 AND the customer is a member,
# or a 10% discount if the purchase is above RS 1000 but the customer is not a member.
# Write a program that takes total_amount and is_member (True/False) as
# input and prints the final amount after applying the correct discount or no discount.
# ANS:
totalAmount = float(input("Enter the total amount: "))
IsMember = input("Are you a member? Yes or No: ").lower()

if totalAmount > 1000:
    if IsMember == 'yes':
        print(f"Final Amount: {totalAmount - (totalAmount * 0.2)}")

    else:
        print(f"Final Amount: {totalAmount - (totalAmount * 0.1)}")

else:
    print(f"Final Amount: {totalAmount}")


# 17. Create a weight conversion program that:
# Asks the user what their Earth weight is (as a float).
# Asks the user for a planet number (as an int).
# Then, use an if/elif/else statement to calculate the user's weight on the destination planet.
# To calculate the user's weight: destination weight=Earth weight × relative gravity
# If the user enters a planet number outside of 1 - 7, print a message
# that says 'Invalid planet number'
# ANS:
userWeight = float(input("Enter your Earth Weight: "))
planetNum = int(input("Enter a planet number, 1 to 7: "))

relativeGravity = {1: 0.38, 2: 0.91, 3: 0.38,
                   4: 2.53, 5: 1.07, 6: 0.89, 7: 1.14}

if planetNum not in relativeGravity:
    print("invalid Planet Number")

else:
    print(
        f"Your weight on planet {planetNum} is {userWeight * relativeGravity[planetNum]} kg")


# 18. WAP which accepts marks of four subjects and display total marks, percentage and grade.
# Hint: more than 70 –> distinction, more than 60 –> first, more than 40 –> pass, less than 40 –> fail.
# ANS:
mark1 = int(input("Enter the marks of the first subject: "))
mark2 = int(input("Enter the marks of the second subject: "))
mark3 = int(input("Enter the marks of the third subject: "))
mark4 = int(input("Enter the marks of the fourth subject: "))

totalMarks = mark1 + mark2 + mark3 + mark4
percentage = (totalMarks/400) * 100

print(f"Total Marks: {totalMarks}")
print(f"Percentage: {percentage}")

if percentage <= 40:
    print("Grade: Fail")

elif percentage > 70:
    print("Grade: Distinction")

elif percentage > 60:
    print("Grade: First Division")

elif percentage > 40:
    print("Grade: Pass")


# 19. Write a Python program to simulate a simple ATM with the following specifications: Assume the card is valid (is_valid = True)
# Initial account balance is RS 5000
# Correct PIN is 123
# After entering correct PIN, display the menu:
# 1. Withdraw
# 2. Check Balance
# 3. Exit
# If user selects 1 then ask amount and deduct from balance.
# If user selects 2 then show current balance.
# If user selects 3 then print Thank you for visiting.
# Show proper messages for wrong PIN and invalid option.
# ANS:
accountBalance = 5000

pin = input("Enter your pin: ")

if pin == '123':
    option = input(
        "Select the appropriate option: 1. Withdraw  2. Check Balance  3. Exit: ")

    if option == 1:
        amount = int(input("Enter a amount to withdraw: "))

        if amount > accountBalance:
            print("Insufficient Funds!")

        else:
            accountBalance -= amount
            print(
                f"Successfully withdrawn Rs. {amount}! New balance is Rs. {accountBalance}")

    elif option == 2:
        print(f"Current balance: {accountBalance}")

    elif option == 3:
        print("Thank you for Visitng!")

    else:
        print("Invalid option!")

else:
    print("Invalid pin! Access Denied!")


# 20. Create a Python program for a text-based adventure game called Magic Forest based on the given flowchart.
# The program should follow the exact logic shown in the flowchart.
# ANS:
print("Welcome to the Magic Forest!")

direction = input("Where do you want to go? North or South?: ").lower()

if direction == 'north':
    choice = input(
        "Cross the River or follow the path? Cross or follow?: ").lower()

    if choice == 'cross':
        print("Game Over!")

    elif choice == 'follow':
        choice = input("Choose from Fairy, Ogre or Elf: ").lower()
        if choice == 'fairy' or choice == 'ogre':
            print("Game Over!")

        elif choice == 'elf':
            print("You Win!")

        else:
            print("Invalid Option!")

    else:
        print("Invalid Option!")

elif direction == 'south':
    print("Game Over!")

else:
    print("Invalid Option! Please choose the right direction")


# 21. Create a Python program for a smart elevator based on the given flowchart.
# The program should follow the exact logic shown in the flowchart.
# ANs:
floorNum = int(input("Enter the floor number: "))

isDoorClosed = True
isRunning = False

if floorNum <= 10 and floorNum >= 0:
    weight = float(input("Enter the total weight: "))
    if weight <= 500:

        if isDoorClosed:
            isRunning = True
        else:
            print("Close the door!")

    else:
        print("Overweight! Lift Cannot Move!")

else:
    print("Invalid Floor Number!")


#
