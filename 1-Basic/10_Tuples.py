"""Tuples"""
# A tuple is a collection of different data types which is ordered and unchangeable (immutable).

name = ('rodrigo', 'mili', 'gonza', 'trini') #round brackets, ()
print(name) # ('rodrigo', 'mili', 'gonza')

# We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). 

empty = tuple()

"""tuples len() functions work"""

print(len(name)) # 3
print(len(empty)) # 0

"""Accessing Tuple Items"""

first_name = name[0]
print(first_name) # rodrigo

"""Slice""" 

# the return value will be a new tuple with the specified items.
second_name = name[1:3]
print(second_name) # ('mili', 'gonza')

"""Tuples to Lists"""

print(id(name)) # 2334052802192 

name = list(name)
print(name) # ['rodrigo', 'mili', 'gonza', 'trini']

print(id(name))

name = tuple(name)
print(name) # ('rodrigo', 'mili', 'gonza', 'trini')
print(id(name)) # 2334052804832 change

"""Item in a Tuple"""

print('rodrigo' in name) # True
print('rodri' in name) # False

"""Join"""

number = (1, 2, 3, 4)
print(name+number) # ('rodrigo', 'mili', 'gonza', 'trini', 1, 2, 3, 4)

name_number = name + number

print(name_number) # ('rodrigo', 'mili', 'gonza', 'trini', 1, 2, 3, 4)

"""Deleting Tuples"""

del number
# print(number) ----> Error