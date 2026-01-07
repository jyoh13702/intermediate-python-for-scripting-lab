import string
import random
def createPassword(length):
    #user_input = input("How many characters do you want in your password? ")
    if not isinstance(length, int) or length <= 8:
        raise ValueError("Password length must be an integer over 8.")

    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return "".join(random.choice(characters) for _ in range(length))
try:
    user_input = input("Enter password length (must be > 8): ")
    length = int(user_input)
    password = createPassword(length)
    print(f"Password: {password}")
except ValueError as error:
    print(f"Error: {error}")

from datetime import datetime
def getDaysBetween(dateA, dateB):
    date_format = '%Y-%m-%d'
    dateObjA = datetime.strptime(dateA, date_format)
    dateObjB = datetime.strptime(dateB, date_format)
    difference = dateObjB - dateObjA
    daysBetween = difference.days
    print(daysBetween)
    return daysBetween

getDaysBetween(input("Enter First Date (YYYY-MM-DD): "), input("Enter Second Date (YYYY-MM-DD): "))

import math
def calculate_circle_area(radius):
    if radius <= 0:
        raise ValueError("Radius must be positive.")

    return math.pi * radius ** 2
try:
    user_input = input("Enter radius: ")
    radius = float(user_input)
    area = calculate_circle_area(radius)
    print(f"The area is: {area}")
except ValueError as error:
    print(f"Invalid input: {error}")