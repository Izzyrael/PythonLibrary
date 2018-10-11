"""
in our last file we capitalized each element of a list,
but what if we have a list of 1000 elements,
we dont want to copy paste that 1000 times
thats why we have loops
"""

# for loops can be kind of tricky
# they read 'for every thing in this big thing, execute the block of code below that is indented'

# lets declare a list to loop through
student_names = ['mark', 'jimmy', 'doug', 'bill']

for name in student_names:
    print("student name: " + name)

# name is a placeholder variable, it is the single item that loops through each time and changes value,
# based on where it is in the loop
# if we run this you'll see that the name variable changes each time, this is because it 'loops' the same code
# until it reaches the end of the list

# but what if we don't have a list and we want to just add some numbers together
# we can do that too, but the format is a bit different

x = 0
for index in range(10):
    x = x + 10
    print('x: {0}'.format(x))

# the range() kinda converts the number we give it, TO A LIST
# this means it will iterate 10 times, because it now has a list of 10 elements
# everytime this loop runs it will add 10 to x and print it
# run this code and try and disect how it works if it is still fuzzy

"""
you also see some weird syntax
the .format() function allows us to plug variables of two different data types, here we want to display what x is
but x is a number, and we want to print a string along with it, so we have to use .format(x) at the end of the string
inside the string we see {0}, this means 'grab the first thing in the .format() function and stick it here
(remember python starts at 0), if we wanted to display more along with x we can do this
"""

x = 0  # remember to reassign x to 0
y = 0
for index in range(10):
    x += 10  # this is short hand notation for 'x = x + 10' we use this to reassign value AND do a math operation
    y += 20
    print('x: {0}, y: {1}'.format(x, y))

# if we run this we see that it'll plug in y as well when we give the string {1}

# range also has a bunch of cool stuff we can do to it,
#    start at 10    end at 20   count by 5
# range( 10,        20,         5)
# this is called 'Overloading', we don't need to use 3 arguments but its useful in case we ever need to

