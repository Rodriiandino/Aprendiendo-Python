"""String"""
# A collection of one or more characters under a single or double quote. If a string is more than one sentence then we use a triple quote.

print('spam eggs') # single quotes

print(""" print on
         several lines """)


# Escape Sequences in Strings
"""
\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")
"""
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

# Reversing a String
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH



# String formatting
# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list)
"""
%s - String 
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision
"""
first_name = 'Rodrigo'
last_name = 'Andino'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string) # I am Rodrigo Andino. I teach Python

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
print(formated_string) # The area of circle with a radius 10 is 314.00.


# New Style String Formatting (str.format)

first_name = 'Rodrigo'
last_name = 'Andino'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b)) # 7
print('{} - {} = {}'.format(a, b, a - b)) # 1
print('{} * {} = {}'.format(a, b, a * b)) # 12
print('{} / {} = {:.2f}'.format(a, b, a / b)) # 1.33
print('{} % {} = {}'.format(a, b, a % b)) # 1
print('{} // {} = {}'.format(a, b, a // b)) # 1
print('{} ** {} = {}'.format(a, b, a ** b)) # 64

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area)
print(formated_string) #The area of a circle with a radius 10 is 314.00.


# String Interpolation
# Another new string formatting is string interpolation, f-strings. 
# Strings start with f and we can inject the data in their corresponding positions.
a = 4
b = 3
print(f'{a} + {b} = {a +b}') # 7 
print(f'{a} - {b} = {a - b}') # 1


