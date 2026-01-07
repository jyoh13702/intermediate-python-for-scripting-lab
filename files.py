def countWords(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
file_name = input("Enter the name of the text file: ")
word_count = countWords(file_name)
if word_count is not None:
    print(f"The file has {word_count} words.")

def listToFile(strings):
    with open("output.txt", "w", encoding="utf-8") as file:
        for s in strings:
            file.write(s + "\n")
    print("The list is written to 'output.txt'.")
userInput = input("Enter strings separated by commas: ")
string_list = [s.strip() for s in userInput.split(",")]
listToFile(string_list)
