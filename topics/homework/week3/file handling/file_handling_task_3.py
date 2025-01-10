# File Handling
# Combine two files into a third file

file_path_1 = "file_to_combine_1"
file_path_2 = "file_to_combine_2"
output_file_path = "output_file"


def combine_files(file_path_1, file_path_2, output_file_path):
    try:
        with open(file_path_1, 'r') as file1, open(file_path_2, 'r') as file2, open(output_file_path,
                                                                                    'w') as output_file:
            file1_content = file1.read()
            file2_content = file2.read()
            output_file.write(file1_content)
            output_file.write(file2_content)
    except FileNotFoundError:
        print("File(s) not found!")
    except PermissionError:
        print("You don't have permission to open this file(s).")


combine_files(file_path_1, file_path_2, output_file_path)
