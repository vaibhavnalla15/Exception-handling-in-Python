""" Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist. """
# exception AttributeError:
# Raised when an attribute reference (see Attribute references) or assignment fails. (When an object does not support attribute references or attribute assignments at all, TypeError is raised.)

def list_operation(num):
    try:
        r = len(num)
        print("Length of the list:- ", r)
    except AttributeError:
        print("Error: The list does not have a 'length' attribute.")

num = [1, 2, 3, 4, 5]
list_operation(num)