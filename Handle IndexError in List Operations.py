""" Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range. """
# exception IndexError:
# Raised when a sequence subscript is out of range. (Slice indices are silently truncated to fall in the allowed range; if an index is not an integer, TypeError is raised.)

def _index(data, index):
    try:
        result = data[index]
        print("Result:-", result)
    except IndexError:
        print("Error: Index out of range.")

num = [1, 2, 3, 4, 5, 6, 7]
index = int(input("Enter the index:- "))
_index(num, index)