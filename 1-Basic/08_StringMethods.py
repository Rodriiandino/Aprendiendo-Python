# String Methods

"""capitalize():"""
# Converts the first character of the string to capital letter
first_name = 'rodrigo'
last_name = 'andino'
print(first_name.capitalize() +" "+ last_name.capitalize()) # 'Rodrigo Andino'

"""count():"""
# returns occurrences of substring in string, count(substring, start=.., end=..). 
# The start is a starting indexing for counting and end is the last index to count.
print(first_name.count('r')) # 2
print(first_name.count('r', 1)) # 1 "odrigo"
print(first_name.count('r', 1, 3)) # 0 "od"

"""endswith():"""
# Checks if a string ends with a specified ending
print(first_name.endswith('go')) # true
print(first_name.endswith('no')) # false

"""expandtabs():"""
# Replaces tab character with spaces, default tab size is 8. 
# It takes tab size argument

full_name ='rodrigo\tAndino'
print(full_name.expandtabs()) #rodrigo Andino


"""find():"""
# Returns the index of the first occurrence of a substring, if not found returns -1
print(full_name.find('o'))  # 1
print(full_name.find('p')) # -1

"""rfind():"""
# Returns the index of the last occurrence of a substring, if not found returns -1
print(full_name.rfind('o'))  # 13
print(full_name.rfind('p')) # -1

"""index():"""
# Returns the lowest index of a substring, 
# additional arguments indicate starting and ending index 
# (default 0 and string length - 1). 
# If the substring is not found it raises a valueError.

print(full_name.index(first_name)) #0
# print(full_name.index(last_name)) #Error 

"""rindex():"""
# Returns the highest index of a substring, 
# additional arguments indicate starting and ending index 
# (default 0 and string length - 1)

"""isalnum():"""
# Checks alphanumeric character
challenge = '30DaysPython'
challenge_2 = '30 Days Python'
print(challenge.isalnum()) # true
print(challenge_2.isalnum()) # false

"""isalpha():"""
# Checks if all string elements are alphabet characters (a-z and A-Z)
print(first_name.isalpha()) #true
print(challenge.isalpha()) #false


"""isdecimal():"""
# Checks if all characters in a string are decimal (0-9)
age = '20'
print(age.isdecimal()) #true
print(first_name.isdecimal()) #false

"""isdigit():"""
# Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
a = 'abc123'
b = '\u00B1'
print(a.isdigit())
print(b.isdigit())

"""isnumeric():"""
# Checks if all characters in a string are numbers or number related (just like isdigit(),
# just accepts more symbols, like ½)

print(first_name.isidentifier()) # true
print(age.isidentifier()) # False, because it is a number

"""islower():""" 
# Checks if all alphabet characters in the string are lowercase
print(first_name.islower()) # true
print(full_name.islower()) # false

"""isupper():"""
# Checks if all alphabet characters in the string are uppercase
c = 'HELLO WORLDS'
print(c.isupper()) # true
print(first_name.isupper()) # false

"""join():""" 
# Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

"""strip():"""
# Removes all given characters starting from the beginning and end of the string
print(first_name.strip('og')) # rodri

"""replace():"""
# Replaces substring with a given string
print(full_name.replace('Andino', 'Sanchez')) # rodrigo Sanchez

"""split():"""
# Splits the string, using given string or space as a separator
print(first_name.split("i")) # ['rodr', 'go']
print(full_name.split("\t")) # ['rodrigo', 'Andino']

"""title():"""
# Returns a title cased string
print(c.title()) # Hello Worlds

"""swapcase():"""
# Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
print(full_name.swapcase()) # RODRIGO aNDINO

"""startswith():"""
# Checks if String Starts with the Specified String
print(c.startswith('HELLO')) #true
print(c.startswith('hello')) #false