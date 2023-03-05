"""List"""

# Python list is an ordered collection which allows to store different data type items. 
# A list is similar to an array in JavaScript.
numbers = [0, 1, 2, 3, 4, 5]  # all are the same data types - a list of numbers
fruit = ['Banana', 'Orange', 'Mango', 'Avocado'] # all the same data types - a list of strings 
differentsData = ['Banana', 10, False, 9.81] # different data types in the list - string, integer, boolean and float

"""Like strings, lists can be indexed and sliced:"""

print(numbers[1]) # 1
print(numbers[-1]) # 5 

# All slice operations return a new list containing the requested elements. 
# This means that the following slice returns a shallow copy of the list:
print(fruit[1:3]) # ['Orange', 'Mango']
print(fruit) # ['Banana', 'Orange', 'Mango', 'Avocado']

"""Lists also support operations like concatenation:"""
print(numbers + fruit) # [0, 1, 2, 3, 4, 5, 'Banana', 'Orange', 'Mango', 'Avocado']


""" Unlike strings, which are immutable, lists are a mutable type, i.e. 
 it is possible to change their content: """
print(numbers) # [0, 1, 2, 3, 4, 5]
print(id(numbers)) # 2250415032832
numbers[0] = 10
print(numbers) # [10, 1, 2, 3, 4, 5]
print(id(numbers)) # 2250415032832
# the ids are the same
 
a = "hols"
print(id(a)) # 2506506366896
a = "hola"
print(id(a)) # 2506506367024

# the ids aren't the same

"""Mytability"""

"""
The following types are mutable:

Listas
Bytearray
Memoryview
Diccionarios
Sets

And they are immutable:

Booleanos
Complejos
Enteros
Float
Frozenset
Cadenas
Tuplas
Range
Bytes
"""

# Immutable types are generally faster to access. 
# So if you don't intend to modify a list, you're better off using a tuple.

# Mutable types are perfect when you want to change their content repeatedly.

# Immutable types are expensive to change, since what you are actually doing is making a copy of their content in a new object with the modifications.

"""List"""

"""You can also add new items at the end of the list, by using the append()"""

numbers[0] = 0
print(numbers) # [0, 1, 2, 3, 4, 5,]
numbers.append(6)
print(numbers) # [0, 1, 2, 3, 4, 5, 6]

"""Assignment to slices is also possible:"""
numbers[0:6] = [10, 9, 8, 7] 
print(numbers) # [10, 9, 8, 7, 6]

numbers[1:4] = []
print(numbers) # [10, 6]

numbers = [0, 1, 2, 3, 4, 5]
print(len(numbers)) # 6

"""It is possible to nest lists (create lists containing other lists):"""
numbers = [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print(numbers) # [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
print(numbers[1]) # [6, 7, 8, 9, 10]
print(numbers[1][0]) # [6]