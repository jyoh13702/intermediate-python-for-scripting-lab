def divide_numbers(n1, n2):
    try:
        result = n1 / n2
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = divide_numbers(numerator, denominator)
    if result is not None:
        print(f"The result is: {result}")
except ValueError:
    print("Invalid input: Please enter numeric values.")

class InvalidEmailError(Exception):
    pass

def validEmail(email):
    if "@" not in email:
        raise InvalidEmailError(f"Invalid Email: '{email}' missing '@")
    return email
try:
    userEmail = input("Enter a valid email address: ")
    validEmail = validEmail(userEmail)
    print(f"Email is valid: {validEmail}")
except InvalidEmailError as e:
    print(e)