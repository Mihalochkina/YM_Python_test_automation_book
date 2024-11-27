# File Handling
# Print out all words with length of n-characters

# Provide the file path and the desired word length here

n = int(input("Enter a desired word length here: "))

file_path = "file_handling_task_2"

def print_words_with_length(file_path, word_lenght):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            words_with_length_n = [word for word in words if len(word) == word_lenght]
            for word in words_with_length_n:
                print(word)
            if not words_with_length_n:
               print("! Words of this length were not found !")
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("You don't have permission to open this file.")

print_words_with_length(file_path, n)

