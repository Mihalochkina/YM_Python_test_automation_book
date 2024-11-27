# File Handling
# Read the file and remove equal lines (if any)

def remove_duplicates(file_path):
    lines = set()
    try:
        with open(file_path, 'r') as file:
            for line in file:
                lines.add(line.strip())

        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("You don't have permission to open this file.")
    return lines


# Provide the file path here
file_path = "file_handling_task_1"

content = remove_duplicates(file_path)
for li in content:
    print(li)

