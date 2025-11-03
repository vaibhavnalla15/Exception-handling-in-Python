""" Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist. """
# exception FileNotFoundError:
# Raised when a file or directory is requested but doesn’t exist. Corresponds to errno ENOENT.

def open_file(filename):
    try:
        file = open(filename, "r")
        contents = file.read()
        print(contents)
        file.close()

    except FileNotFoundError:
        print("Error: File not found.")

file_name = input("Enter a file name:- ")
open_file(file_name)