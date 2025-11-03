""" Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue. """
# exception PermissionError:
# Raised when trying to run an operation without the adequate access rights - for example filesystem permissions.

def open_file(filename):
    try:
        with open(filename, "w") as file:
            contents = file.read()
            print(contents)
    except PermissionError:
        print("Error: Permission denied to open the file.")

file_name = input("Enter a file_name:- ")
open_file(file_name)