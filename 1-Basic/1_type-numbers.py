# Hola Mundo "Comentario"

# The equal sign (=) is used to assign a value to a variable.

#Variable
spam = "spam"  # and this is the second comment
          # ... and now a third!
          
text = "# This is not a comment because it's inside quotes."

"""This is multiline comment
multiline comment takes multiple lines.
python is eating the world
"""

print("Hello Worlds") #print to console
print(spam)
print(text)

#NUMBERS

print(2 + 3)   # "5" addition(+) 
print(3 - 1)   # "2" subtraction(-)
print(2 * 3)   # "6" multiplication(*)
print(3 / 2)   # "1.5" division(/) # division always returns a floating point number
print(3 ** 2)  # "9" exponential(**)
print(3 % 2)   # "1" modulus(%) returns the remainder of the division
print(3 // 2)  # "1" Floor division operator(//)
print(17 // 3)  # "5" return an Int
print((50 - 5*6) / 4) # "5.0" parentheses (()) can be used for grouping


# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type((50 - 5*6) / 4))      # Float # division always returns a floating point number
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

"""Number"""
# Integer: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...
# Float: Decimal number Example ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
# Complex Example 1 + j, 2 + 4j


"""String"""
# A collection of one or more characters under a single or double quote. If a string is more than one sentence then we use a triple quote.


"""Booleans"""
# A boolean data type is either a True or False value. T and F should be always uppercase.
#True  #  Is the light on? If it is on, then the value is True
#False # Is the light on? If it is off, then the value is False


"""List"""
# Python list is an ordered collection which allows to store different data type items. A list is similar to an array in JavaScript.
# [0, 1, 2, 3, 4, 5]  # all are the same data types - a list of numbers
# ['Banana', 'Orange', 'Mango', 'Avocado'] # all the same data types - a list of strings (fruits)
# ['Banana', 10, False, 9.81] # different data types in the list - string, integer, boolean and float


"""Dictionary"""
# A Python dictionary object is an unordered collection of data in a key value pair format.
# {
# 'first_name':'Asabeneh',
# 'last_name':'Yetayeh',
# 'country':'Finland', 
# 'age':250, 
# 'is_married':True,
# 'skills':['JS', 'React', 'Node', 'Python']
# }


"""Tuple""" 
# A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.
# ('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya') # Names They are immutable.


"""Set"""
# A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.



