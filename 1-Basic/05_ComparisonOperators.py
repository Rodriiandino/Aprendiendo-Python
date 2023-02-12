# In programming we compare values, we use comparison operators to compare two values. 
# We check if a value is greater or less or equal to other value. 

# This will return a boolean

print(3 > 2)     # True, because 3 is greater than 2
print(3 > 3)     # False
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2

# len() It tells you the size of the string and list.
print(len('Mango')) #5
print(len([1,2,3,4,5])) #5

print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# In addition to the above comparison operator Python uses:

# is: Returns true if both variables are the same object(x is y)
# is not: Returns true if both variables are not the same object(x is not y)
# in: Returns True if the queried list contains a certain item(x in y)
# not in: Returns True if the queried list doesn't have a certain item(x in y)

print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# == is used to compare values. It is used when you want to know if two variables have the same value.
# It is used is to compare objects.
# It is used when you want to know if two variables literally refer to the same object.
a = [1, 2]
b = [1, 2]
print(a is b) # False "is" True will be returned if the two variables point to the same object.
print(a == b) # True "==" will return True if the values of the variables are equal.
