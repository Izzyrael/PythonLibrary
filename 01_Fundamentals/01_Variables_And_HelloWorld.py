# a pound sign is a Single Line Comment
"""
this is a multi-line comment
doo doo doo
"""

# Comments do not get executed
# MAKE SURE TO ADD A SPACE AFTER #

# you do not need to declare what data type the variable will be in python unlike other languages
# to create a variable, type the new name and give it a value
variable_one = 5

# variables can be any value and can change from a number to a string (strings are words and characters)and vice versa
# when you are working with strings you can use '' or "" to tell python that its a strings
# a major difference in strings is that strings do not have any numerical value unlike numbers
variable_one = "Hello"

# we can add variables together by using a plus sign

a = 2
b = 2

c = a + b

# now we can use the print() function to display our new variable c

print(c)

# at the top of PyCharm click on "Run" and "Run" again
# click on this files name, a window should appear at the bottom and show 4, our variable c

# now lets change c to a string just like we did to variable_one

c = "World"

# and now lets see what happens when we try to add two strings together

hello_world = variable_one + c

# and then display it in our console using print()
print(hello_world)

# run this in your console and see what happens

# MATH OPERATORS:
# in python we have close to the same syntax for doing math with our variables,
# the following diagram will show you what each symbol means

# + plus
# - minus
# / divide
# * multiply
# % MODULUS ( it means give the remainder as the answer 5 % 2 = 1
# ++ increment by one
# -- decrement by one

# we also have the addition/subtraction assignment operators
# lets look at this line of code

assign = 15
assign += 5

print(assign)

# we get 20! but before we would've had to write it like this
# assign = assign + 5
# we just get rid of the middle part and smush it together, they run the exact same but one is shorter

# when you feel ready try and complete Challenge 1 in 17_challenges.txt
