# function
""""
In Python we have lots of built-in functions. 
Built-in functions are globally available for your use that mean
you can make use of the built-in functions without importing or configuring. 
"""
# Print function takes unlimited number of arguments. 
# An argument is a value which we can be passed or put inside 
# the function parenthesis.

# example basic

print("Hello World", "Bye Moon") # it can take multiple arguments
print(type(10))  # Checks the data type and it takes only one argument

print(str(10))  #Converts number to string
print(type(str(10))) #String

print(int("10"))  #Converts string to number 
print(type(int("10"))) #int

print(float(10)) #Converts int to float
print(type(float(10))) #float

# Casting: Converting one data type to another data type.
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Rodrigo'
print(first_name)               # 'Rodrigo'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['R', 'o', 'd', 'r', 'i', 'g', 'o']

# Getting user input using the input() built-in function. Let us assign the data we get from a user.

name = input("What's your name? ") #It takes user input

print("hello, " + name) # Demonstrates concatenation of strings

print(f"hello, {name}") # Demonstrates a format string


# More built-in functions
print(min(20, 30, 40)) #Gives the minimum value
print(min([20, 30, 40])) #Gives the minimum value

print(max(20, 30, 40)) #Gives the Maximum value
print(max([20, 30, 40])) #Gives the Maximum value

print(sum([20, 30, 40] )) #Takes only list as an argument and return the sum

#Python has over 69 Built-in Functions
