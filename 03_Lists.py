
# Lists are a type of collection, we will get into other types that python has to offer later on
# To make a new list all we have to do is give it some square brackets

empty_list = []
# this is a list with nothing in it

list_with_stuff = ['this', 'list', 'has', 'stuff']
# this list has stuff in it, specifically it is a list of STRINGS

# you can add stuff to lists like so
empty_list.append(1)

# this will add 1 to our list, you can have many different data types in a list
# append() will add stuff to the list, ( append('a thing') to the list empty_list)

# we can also split strings into lists
string = 'this is a long string with lots of words'
string_list = string.split(' ')

print(string_list)

# if we run this we see that it 'split' the string into a list, this also shows that we can print() a list too
# to see whats in it

# while we're at it lets see some other string functions we can use
capitalize = 'capitalize'.capitalize()
replace = 'replace'.replace('e', 'a')
is_alpha = 'hello'.isalpha()  # this checks if the string has value, or is a truthy string
is_digit = '123'.isdigit()  # checks to see if the string can be converted to a numerical value

print(capitalize)
print(replace)
print(is_alpha)
print(is_digit)

# run this and see how the code works

# now what if we have a user enter their name, we want to capitalize it right?
# we can do this with lists

full_name = 'billy bob'
full_name_list = full_name.split(' ')

# so now we have a list with 2 values, their first and last name
# so now we have to capitalize everything in the list!
# we do this by calling the 'index' of the item in the list
full_name_list[0] = full_name_list[0].capitalize()
full_name_list[1] = full_name_list[1].capitalize()

# the index is the specific spot an item is in a list, all lists in python start at 0
# what we did was reassign the specific index to the capitalized version of itself inside the list
# that's why we typed full_name_list[0/1] twice
# so if we print this to our console we'll see that they are now capitalized :D

print(full_name_list)

