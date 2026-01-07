def validate_age(age):
    """
    Validates that the provided age is a positive integer.
    Uses the parameter age to return the positive integer age value
    Raises a ValueError if age is not an integer or if its lass than or equal to zero.
    """
    if not isinstance(age, int):
        raise ValueError("Age must be an integer.")    
    if age <= 0:
        raise ValueError("Age must be a positive integer.")    
    return age

try:
    user_input = input("Enter age: ")
    age = int(user_input)  # convert input to integer
    valid_age = validate_age(age)
    print(f"Your age is valid: {valid_age}")

except ValueError as error:
    print(f"Invalid input: {error}")

import math
def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def get_area(shape, *args):
    if shape == "rectangle":
        return calculate_rectangle_area(args[0], args[1])
    elif shape == "circle":
        return calculate_circle_area(args[0])
    else:
        raise ValueError("Invalid shape")

shape = input("Enter shape (rectangle or circle): ").strip().lower()
if shape == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = get_area(shape, length, width)
elif shape == "circle":
    radius = float(input("Enter radius: "))
    area = get_area(shape, radius)
else:
    print("Invalid shape")
    area = None
if area is not None:
    print(f"The area of the {shape} is {area}")
