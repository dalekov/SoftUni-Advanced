import os

# Set the directory to be traversed
directory = "/Users/denis.alekov1/PycharmProjects/SoftUni-Advanced/07_File_Handling/Exercise/04"

# Initialize a dictionary to store files by extension
files_dict = {}

# Walk through the directory and its subdirectories
for root, dirs, files in os.walk(directory):
    for file in files:
        # Get the file extension
        extension = os.path.splitext(file)[1]

        # If the extension is not already in the dictionary, add it with an empty list
        if extension not in files_dict:
            files_dict[extension] = []

        # Exclude the specific file '04_directory_traversal.py' from the list
        if file != '04_directory_traversal.py':
            files_dict[extension].append(file)

# Initialize a list to store the formatted output
output = []

# Sort the dictionary items by extension and process each one
for extension, files_list in sorted(files_dict.items(), key=lambda x: x[0]):
    # Append the extension to the output list
    output.append(extension)

    # Sort the files under each extension and add them to the output list with proper indentation
    for file in sorted(files_list):
        output.append(f"- - - {file}")

# Write the output to a file named 'report.txt'
with open("report.txt", "w") as output_file:
    # Join the output list with newline characters and write it to the file
    output_file.write("\n".join(output))
