""" Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue. """
# exception UnicodeDecodeError:
# Raised when a Unicode-related error occurs during decoding. It is a subclass of UnicodeError.


def open_file(filename):
    encoding = input("Input the encoding (ASCII, UTF-16, UTF-8) for the file: ")
    try:
        with open(filename, 'r', encoding=encoding) as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except UnicodeDecodeError:
        print("Error: Encoding issue occurred while reading the file.")

file_name = input("Input the file name: ")
open_file(file_name)
