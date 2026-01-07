def primeNumber(number):
    if number < 2:
        raise ValueError("Numbers less than 2 cannot be prime.")

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
try:
    userInput = int(input("Enter a number: "))
    if primeNumber(userInput):
        print(f"{userInput} is a prime number.")
    else:
        print(f"{userInput} is not a prime number.")

except ValueError as e:
    print(f"Invalid input: {e}")

def displayDictionary(data):
    if not isinstance(data, dict):
        print("Input must be a dictionary")
        return
    for key, value in data.items():
        print(f"Key: {key}, Value: {value}")
userInput = input("Enter dictionary items in key:value format with commas: ")
try:
    userDict = {}
    for item in userInput.split(","):
        key, value = item.split(":")
        key = key.strip()
        value = value.strip()
        if value.isdigit():
            value = int(value)
        else:
            try:
                value = float(value)
            except ValueError:
                pass 
        userDict[key] = value
    displayDictionary(userDict)
except Exception as e:
    print(f"Invalid input format: {e}")

def displayNumbersTo(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("The number must be a positive integer.")
    current = 1
    while current <= number:
        print(current)
        current += 1
while True:
    try:
        userInput = int(input("Enter a positive integer: "))
        displayNumbersTo(userInput)
        break  
    except ValueError as e:
        print(f"Invalid: {e}")