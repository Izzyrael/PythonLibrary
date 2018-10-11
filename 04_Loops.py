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

# but what if we want to find one specific value and leave the loop cause we just need 1 thing?
# this is where the keyword 'break' comes in

for index in range(2, 12):
    print(index)
    if index == 7:
        break

# if we run this we see that it gets to 7 but doesn't finish at 12, why is that?
# its because we told it to break IF the placeholder 'index' is equal to 7
# that's right we can put IF statements inside of FOR loops, that's called 'nesting'

# now lets say we want to skip a specific element, lets use student names for this example

student_names.append('connor')
student_names.append('matt')
student_names.append('lawrence')

for name in student_names:
    if name == 'connor':
        continue
    print(name)

# continue means 'skip the rest of this loop and CONTINUE to the next element,
# this means that if the condition ( name is equal to connor ) is met, it will skip and NOT print
# lets run it and see if connor shows up

"""
Now we're going to cover while loops
while loops read as 'WHILE something is true, do this
"""

x = 0
while x < 10:  # while x is less than 10, print 'x: {x}' and add 1 to x
    print('x: {0}'.format(x))
    x += 1
print('operation complete')

# also note the big difference in a while loop, we have to auto increment our variable we are testing
# just to clarify that this is looping we won't see 'operation complete' until we see 9
# if we run this we can see it in action

# WE CAN ALSO DO INFINITE LOOPS
# these can be dangerous so be careful and get that stop button ready
# an infinite loop is a loop that never ends

no_value = None
x = 0
while not no_value:
    x += 1
    print(x)
    break  # remove this break statement to see what an infinite loop looks like

# if we run this, and stop it after a couple seconds we can see it runs for a while
# be careful of infinite loops as they can be hard to detect

# we can use the break keyword to get out of our infinite loops

x = 0
while True:  # this loop is infinite because we are not changing this True value
    if x == 42:
        break  # even though the loop is infinite we break out of it when x reaches 42 because the IF condition is met
    print(x)
    x += 1

# run it and disect this code until you fully understand exactly whats going on heres
