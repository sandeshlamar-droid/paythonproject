# 1no.question
# students_email = {'ranb': 'ramblama@gmail.com',
#                   'duck': 'ducklama@gmail.com',
#                   'licx': 'licxlama@gmail.com'}
# name = input('enter your email:')
# print(students_email.get('name', 'user noy found:'))


# 2no.question
shoppinng_list = {"milk", "bread", "eggs"}
bought = {"bread", "eggs"}
unbought = {"milk"}
missing_items = shoppinng_list.isdifference(bought)
if not missing_items:
    print("missing_items:", missing_items)
else:
    print("shopping complete.")


# 3no.question
class_list = {"ram", "sita", "laxman"}
new_student = input("Enter the name of the new student: ")
if new_student not in class_list:
    class_list.add(new_student)
    print("Student added successfully.")
else:
    print("Student already present.")
print("Updated class list:", class_list)


# 4no.question
votes = ["Blue", "Red", "Blue", "Green", "Blue"]
blue_count = votes.count("Blue")
if blue_count >= 3:
    print("Blue wins.")
else:
    print("Blue did not win.")

# 5. Using a dictionary of student grades

grades = {"ram": 92, "sita": 88}
student_name = input("Enter the student's name: ")
if student_name in grades:
    print(f"{student_name}'s grade: {grades[student_name]}")
else:
    print("Grade not available.")

# 6. A company accepts an application only if:
# applicant = {"name": "Priya", "skills": ["sql", "Java"], "experience_years": 1}
# required_skills = {"Python", "Java"}
# The candidate knows Python or Java, and has at least 2 years of experience.
# Check if at least one skill in applicant[‘skills’] is in required_skills, and
# experience >= 2. Print priya qualifies or priya does not qualify.
applicant = {"name": "Priya", "skills": ["sql", "Java"], "experience_years": 1}
required_skills = {"Python", "Java"}
if required_skills.intersection(applicant["skills"]) and applicant["experience_years"] >= 2:
    print("Priya qualifies.")
else:
    print("Priya does not qualify.")

# 7. Write a Python program that determines whether an airline passenger’s
# cabin baggage is allowed based on two rules: The baggage weight must be 7
# kg or less. The item being carried must not be in banned_items.
# banned_items = {"scissors", "knife", "lighter"}
# Prompt the user to enter the baggage weight and the name of the item.
# Convert the item input to lowercase to ensure case-insensitive comparison.
# If both conditions are satisfied weight <= 7 and item not banned, print Bag
# allowed. Otherwise, print Bag not allowed.
banned_items = {"scissors", "knife", "lighter"}
baggage_weight = float(input("Enter baggage weight in kg: "))
item = input("Enter the name of the item: ").lower()

if baggage_weight <= 7 and item not in banned_items:
    print("Bag allowed.")
else:
    print("Bag not allowed.")

# 8. Write a program to change shyam salary to 8500 in the following dictionary.
# Given:
# sample_dict = {
# 'emp1': {'name': 'john', 'salary': 7500},
# 'emp2': {'name': 'Emma', 'salary': 8000},
# 'emp3': {'name': 'shyam', 'salary': 500}0}
sample_dict = {
    'emp1': {'name': 'john', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'shyam', 'salary': 5000}
}
sample_dict['emp3']['salary'] = 8500
print(sample_dict)

# 9. Store two sets of items for Ram and Laxman. Determine if they have zero
# items in common. Print they picked completely different items or they
# have some common items based on the result
ram_items = {"apple", "banana", "orange"}
laxman_items = {"grape", "melon", "orange"}
common_items = ram_items.intersection(laxman_items)
if common_items:
    print("They have some common items:", common_items)
else:
    print("They picked completely different items.")

# 10.Your task is to write a script that validates an incoming access token and
# determines the correct network path using three specific checks. The
# program should follow the exact logic shown in the flowchart.
my_list = [10, 20, 30]
my_tuple = (10, 20, 30)
my_set = {30, 40}
my_dict = {'a': 10, 'b': 20}

val = 20


if val in my_list and val in my_tuple:

    if 'b' in my_dict and val not in my_set:
        print("Path A")

    else:
        print("Path B")

else:
    print("Path C")

# 11.What happens when you initialize a dictionary with duplicate keys, like this:
# data = {'a': 10, 'b': 20, 'a': 30}
# The first value 10 is kept and the second 30 is ignored.
# The value for a becomes 30.
# The dictionary will contain both instances of 'a'.
data = {'a': 10, 'b': 20, 'a': 30}
print(data)

# 12.Which of these cannot be used as a key in a Python dictionary?
# 10.5
# (1,2,3)
# [1,2,3]
# ‘key’
# The list [1,2,3] cannot be used as a key in a Python dictionary
# because it is mutable and unhashable. The other options (10.5, (1,2,3), and
# 'key') can be used as keys since they are immutable and hashable.

# 13.What is the output of the following?
# d = {'val': 10}
# if d.get('score')
#   print("Found")
# else:
#   print("Not Found")
# KeyError
# 10
# Not Found
# Found
# The output will be "Not Found"

# 14. Given items = [10, 10, 20]. What is the result of len (set (items))?
# 0
# 1
# 2
# 3
# The result will be 2

# 15.Which code snippet correctly adds 40 to the existing my_set = {10, 20, 30}?
# my_set.append(40)
# my_set = my_set + {40}
# my_set[3] = 40
# my_set.add(40)
# The correct code snippet is: my_set.add(40)

# 16.Create a dictionary menu where Pizza is 15, Burger is 10, and Salad is 8. Set
# order = ‘Pizza’. Write a program that checks if the order exists as a key in
# the menu. If it does, print the price of that item; if not, print item not found.
menu = {'Pizza': 15, 'Burger': 10, 'Salad': 8}
order = 'Pizza'

if order in menu:
    print(f"The price of {order} is ${menu[order]}.")
else:
    print("Item not found.")

# 17.Initialize a dictionary
 # student_data = {'name': 'sam', 'score': 85}
# Write a program that checks if the score is greater than or equal to 80. If it
# is, add a new key status to the dictionary with the value Pass. If not, set
# status to Review. Print the final dictionary.
student_data = {'name': 'sam', 'score': 85}
if student_data['score'] >= 80:
    student_data['status'] = 'Pass'
else:
    student_data['status'] = 'Review'
print(student_data)

# 18.Define a dictionary
# database = {"admin": "1234", "user1": "abcd"}
# Define two variables
# input_user = "admin"
# input_pass = "1234"
# Write a conditional that checks if the input_user exists in the database and
# if the password matches the value stored for that user. Print Login
# Successful or Login Failed.
database = {"admin": "1234", "user1": "abcd"}
input_user = "admin"
input_pass = "1234"

if input_user in database and database[input_user] == input_pass:
    print("Login Successful")
else:
    print("Login Failed")

# 19.Initialize a list emails and initialize a set blacklisted emails.
# emails = ["ram123@test.com", "hari77@test.com"]
# blacklisted = {"hari77@test.com"}
# Set current_email = ‘hari77@test.com’.
# Write a program that checks if current_email is in all_emails but not in
# blacklisted. Print "Email Sent" if safe, or "Blocked" if it fails either condition.
emails = ["ram123@test.com", "hari77@test.com"]
blacklisted = {"hari77@test.com"}
current_email = "hari77@test.com"

if current_email in emails and current_email not in blacklisted:
    print("Email Sent")
else:
    print("Blocked")

# 20.Write a script to check if the target key exists in inventory. If it exists, check
# if the target is not in restricted_zones and the value in inventory is greater
# than 0.
# Print dispatch item if all conditions pass. Print stock error if it fails the
# inner check, and invalid zone if it fails the outer check.
# inventory = {'A1': 50, 'B2': 0, 'C3': 10}
# restricted_zones = {'B2', 'Z9'}
# target = 'B2'
inventory = {'A1': 50, 'B2': 0, 'C3': 10}
restricted_zones = {'B2', 'Z9'}
target = 'B2'
if target in inventory:
    if target not in restricted_zones and inventory[target] > 0:
        print("Dispatch item.")
    else:
        print("Stock error.")

else:
    print("Invalid zone.")

# 21.You are developing a student enrollment module. The system must verify
# course availability and student eligibility using different Python collection
# types to ensure data integrity. Write a Python script that implements an
# enrollment gatekeeper using the following requirements.
# Create a set called valid_courses containing python, robotics, java and create
# a list called hs_grades containing integers 9 through 12.
# Capture and Store Data, use input() to collect a student's name, course, and
# grade as an integer. Store these three values inside a single Dictionary
# named student_records. Use if-else statements to evaluate the data in this exact order
# 1. Check if the requested course exists in the valid_courses set. If not,
# print:{name} selected an invalid course.
# 2. If the course is valid, check if the student's grade is within the hs_gradeslist.
# # If the grade is less than 9, print grade too low and if greater than 12,print grade too high.
# 3. If they pass both checks, apply the robotics rule, if the course is roboticsand the grade is 9, they are ineligible.
# If they pass, print {name} is approved for {course}
# If they fail, print {name} is not eligible for {course} grade too low.
valid_courses = {"python", "robotics", "java"}
hs_grades = [9, 10, 11, 12]
student_records = {}
name = input("Enter student's name: ")
course = input("Enter course: ")
grade = int(input("Enter grade (9-12): "))
student_records[name] = {'course': course, 'grade': grade}
if course not in valid_courses:
    print(f"{name} selected an invalid course.")
elif grade < 9:
    print("Grade too low.")
elif grade > 12:
    print("Grade too high.")
else:
    if course == "robotics" and grade == 9:
        print(f"{name} is not eligible for {course} grade too low.")
    else:
        print(f"{name} is approved for {course}.")
