"""String"""
# A collection of one or more characters under a single or double quote. If a string is more than one sentence then we use a triple quote.

print('spam eggs') # single quotes

print(""" print on
         several lines """)

print('doesn\'t') # use \' to escape the single quote...
print("doesn't") # ...or use double quotes instead
print('"Isn\'t," they said.') #combination
print('First line.\nSecond line.') # \n means newline
print(r'C:\some\name') # If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote

# Strings can be concatenated (glued together) with the + operator, and repeated with *:
print("Rodr" + (2 * "i")) #Rodrii
# automatically concatenated.
print("Rodr" "ii") #Rodrii
# This only works with two literals though, not with variables or expressions
