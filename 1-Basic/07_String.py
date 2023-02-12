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


# This feature is particularly useful when you want to break long strings:
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)


# Strings can be indexed (subscripted), with the first character having index 0. 
word = 'Python'
print(word[0]) # P
print(word[5]) # n

print(word[-1]) # last character //n
print(word[-2]) # second-last character //o
print(word[-6]) # P

# In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain substring:
print(word[0:2]) # Py
print(word[2:5]) # thon

print(word[:2])    # character from the beginning to position 2 (excluded) //Py
print(word[4:])   # characters from position 4 (included) to the end //on
print(word[-2:])   # characters from the second-last (included) to the end //on

# Note how the start is always included, and the end always excluded.
print(word[:2] + word[2:]) # Python
print(word[:4] + word[4:]) # Python



