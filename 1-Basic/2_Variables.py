# Variables
"""
Variables store data in a computer memory.
Mnemonic variables are recommended to use in many programming languages. 
A mnemonic variable is a variable name that can be easily remembered and associated. 
A variable refers to a memory address in which data is stored.
"""
# Number at the beginning, special character 
# hyphen are not allowed when naming a variable. 
# A variable can have a short name (like x, y, z)
# but a more descriptive name (firstname, lastname, age, country) is highly recommended.

# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )

# The equal sign (=) is used to assign a value to a variable.

# example
first_name = 'Rodrigo' #String
last_name = 'Andino'
country = 'Argentina'
city = 'Cordoba'

age = 20 #Number

is_married = False #Boolean

skills = ['HTML', 'CSS', 'JS', 'React', 'Python'] #Array or List

person_info = { #Dictionary or Objet
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }


# Printing the values stored in the variables
print('First name:', first_name)
print(last_name, first_name, age)

# Declaring multiple variables in one line

first_name, last_name, age = 'Agustin', 'Sanchez', 20
print(first_name, last_name, age)


# reserved words
"""
False 

None 

True 

__peg_parser__ 

And 

As 

Assert 

Async 

Await 

Break 

Class 

Continue 

Def 

Del 

Elif 

Else 

Except 

Finally 

For 

From 

Global 

If 

Import

In 

Is 

Lambda 

Nonlocal 

Not 

Or 

Pass 

Raise 

Return 

Try 

While 

With

Yield 
"""