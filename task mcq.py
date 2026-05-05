# Q1. Write a program to check whether the given number is in between 1 and 100 or not.

num = int(input("Enter a number: "))

if num >= 1 and num <= 100:
    print(f"{num} is between 1 and 100")

else:
    print(f"{num} is not between 1 and 100")

# Q2. Check whether the user input number is even or odd and display it to user.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even")

else:
    print(f"{num} is odd")

# Q3. Write a program that asks the user for a number in the range of 1 to 12.
# The program should display the corresponding month, where 1=january, 2=february,
# 3=march,4=april,5=may,6=june,7=july, 8=august,9=september,10=october,11=november,12=december.
# The program should display an error  message if the user enters a number that is outside the
# range of 1 to 12.

num = int(input("Enter a number: "))
month = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
         7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

if num in month:
    print(f"{num} = {month[num]}")

else:
    print(f"{num} is invalid!")

# Q4. A school has following rules for grading system:
# Below 25 - F,  25 to 45 - E, 45 to 50 - D, 50 to 60 - C
# 60 to 80 - B, Above 80 - A, Ask user to enter marks and print the corresponding grade.

marks = int(input("Enter your marks: "))

if marks >= 80:
    print("Grade: A")

elif marks >= 60:
    print("Grade: B")

elif marks >= 50:
    print("Grade: C")

elif marks >= 45:
    print("Grade: D")

elif marks >= 25:
    print("Grade: E")

elif marks < 25:
    print("Grade: F")

else:
    print("Invalid Marks!")

# Q5. Write a program to check whether a number is divisible by
# 7 or not.

num = int(input("Enter a number: "))

if num % 7 == 0:
    print(f"{num} is divisible by 7")

else:
    print(f"{num} is not divisible by 7")

# Q6. Write a program to accept two numbers and mathematical operators and
# perform operation accordingly.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = str(input("Enter the operator: "))

if operator == "+":
    print(f"Your Answer is: {num1 + num2}")

elif operator == "-":
    print(f"Your Answer is: {num1 - num2}")

elif operator == "*":
    print(f"Your Answer is: {num1 * num2}")

elif operator == "/":
    print(f"Your Answer is: {num1 / num2}")

elif operator == "%":
    print(f"Your Answer is: {num1 % num2}")

elif operator == "**":
    print(f"Your Answer is: {num1 ** num2}")

elif operator == "//":
    print(f"Your Answer is: {num1 // num2}")

else:
    print(f"{operator} is not a valid arithmetic operator.")

# Q7. Write a Python program to check car loan eligibility:
# Salary >= 50,000 and Credit Score >= 700: "Eligible"
# Otherwise: "Not Eligible"

salary = int(input("Enter your salary: "))
creditScore = int(input("Enter your Credit Score: "))

if salary >= 50000 and creditScore >= 700:
    print("Eligible for car loan")

else:
    print("Not Eligible for car loan")

# Q8. Write a Python program that takes an integer input n
# From given number, check if it is divisible by both 3 and 5, and print "FizzBuzz" if true.
# If the number is divisible only by 5, print "Buzz." If it is  divisible only by 3, print "Fizz."
# Finally, if the number is not divisible by either 3 or 5, print the number itself.

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")

elif num % 5 == 0:
    print("Buzz")

elif num % 3 == 0:
    print("Fizz")

else:
    print(num)

# Q9. Write a Python program that takes a character input and checks whether it is a vowel or consonant.

vowel = ["a", "e", "i", "o", "u"]

char = input("Enter a character: ").lower()

if len(char) != 1:
    print(f"{char} is not a single character: ")

elif char in vowel:
    print(f"{char} is a vowel")

else:
    print(f"{char} is a consonant")

# Q10. Write a Python program to input marks and determine the grade based on the following conditions:
# 90-100: A, 80-89: B, 70-79: C, Below 70: Fail

marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade: A")

elif marks >= 80:
    print("Grade: B")

elif marks >= 70:
    print("Grade: C")

elif marks < 70:
    print("Fail")

else:
    print("Invalid Marks")

# Q11. Write a Python program to categorize a person’s age:
# Age < 13: Child, 13 <= Age <= 19: Teenager, Age > 19: Adult

age = int(input("Enter age: "))

if age < 13:
    print("Child")

elif 13 <= age <= 19:
    print("Teenager")

else:
    print("Adult")

# Q12. Write a Python program to check if a given character is uppercase, lowercase, or a digit.

data = input("Enter a character: ")

if data.islower():
    print(f"{data} is in lowercase")

elif data.isupper():
    print(f"{data} is in uppercase")

elif data.isdigit():
    print(f"{data} is a digit")

# Q13. Write a Python program that takes a color as input ("Red", "Yellow", "Green")
# and outputs the corresponding action ("Stop", "Get Ready", "Go").

color = input("Enter a color Red, Yellow or Green: ").title()

traffic = {"Red": "Stop", "Yellow": "Get Ready", "Green": "Go"}

if color in traffic:
    print(f"{traffic[color]}")

else:
    print("Invalid color")

# Q14. Write a Python program to check eligibility for a job based on age and experience:
# Age > 18 and Experience >= 2 years: Eligible
# Otherwise: Not Eligible


age = int(input("Enter your age: "))
exp = int(input("Enter your amount of experience in years: "))

if age > 18 and exp >= 2:
    print("You are eligible for the job")

else:
    print("You are not eligible for the job")

# Q15. Write a Python program to give advice based on the temperature:
# Temperature > 30°C: "It's hot, stay hydrated!"
# Temperature between 15-30°C: "Enjoy the weather!"
# Temperature < 15°C: "It's cold, wear warm clothes!"

temp = int(input("Enter the temperature in Celsius: "))

if temp > 30:
    print("It's hot, stay hydrated!")

elif 15 < temp < 30:
    print("Enjoy the weather!")

elif temp < 15:
    print("It's cold, wear warm Clothes!")

# Q16. Write a Python program that takes a menu option ("Pizza", "Burger", "Pasta") and prints its price:
# Pizza: $10, Burger: $7, Pasta: $8

menu = {"Pizza": "$10", "Burger": "$7", "Pasta": "$8"}

user = input("Enter one of the menu options Pizza, Burger or Pasta: ").title()

if user in menu:
    print(f"{user}: {menu[user]}")

else:
    print(f"{user} is not a valid menu option!")

# Q17. Write a Python program to select players based on height:
# Height >= 6 feet: Selected, Height < 6 feet: Not Selected

height = float("Enter your height: ")

if height >= 6.0:
    print("You are Selected")

elif height < 6.0:
    print("Your are not Selected")

# Q18. Write a Python program to check if a person is eligible to watch a movie based on their age:
# Age >= 18: Allowed, Age < 18: Not Allowed

age = int(input("Enter your age: "))

if age >= 18:
    print("You are allowed to watch the movie")

elif age < 18:
    print("You are not allowed to watch the movie")

# Q19. Write a Python program to check login credentials:
# Username: "admin", Password: "password123"
# If correct, print "Access Granted"; otherwise, print "Access Denied."

username = "admin"
password = "password123"

givenUser = input("Enter your username: ")
givenPassword = input("Enter your password: ")


if givenUser == username and givenPassword == password:
    print("Access Granted")

elif givenUser != username:
    print("Incorrect Username! Access Denied.")

elif givenPassword != password:
    print("Incorrect password! Access Denied.")

# Q20. Write a Python program that takes a month number (1–12) and outputs the corresponding season:
# 12, 1, 2: "Winter", 3, 4, 5: "Spring", 6, 7, 8: "Summer"
# 9, 10, 11: "Autumn"

season = {
    "12": "Winter", "1": "Winter", "2": "Winter",
    "3": "Spring", "4": "Spring", "5": "Spring",
    "6": "Summer", "7": "Summer", "8": "Summer",
    "9": "Autumn", "10": "Autumn", "11": "Autumn"
}

data = input("Enter the month in number form: ")

if data in season:
    print(f"{data}: {season[data]}")

else:
    print(f"{data} is invalid!")
