numbers_dictionary = {}

line = input()

while line != "Search":
    # Saving the input in a variable so we can search the dict by key
    number_as_string = line


    try: # If the user inputs is numeric, we extract the key:value pair from dict
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError: # If user input is non-numeric
        print("The variable number must be an integer")

    # Taking another input to keep the loop going.
    line = input()

# If 'Search' is encountered, we need to start the second loop by taking another line of input:
line = input()
while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError: # If the key is not found in the dict:
        print("Number does not exist in dictionary")

    # Keep the loop going:
    line = input()

# If 'Remove' is encountered, we need to start the third and final loop by taking another line of input:
line = input()
while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched] # Delete key if found
    except KeyError: # If the key, is not found in the dict:
        print("Number does not exist in dictionary")

    # Keep the loop going:
    line = input()

# Printing final result:
print(numbers_dictionary)
