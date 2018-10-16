
"""
Now that we know variables lets do something with them,
A conditional is when we check the truthy-ness of a value,
in python IF a number has a value and is not 0, it is TRUTHY
lets do that now
"""

truthy_num = 15

if truthy_num:
    print('it is truthy')

"""
notice the indent and the colon, python doesnt use square brackets. a good way to remember this is if you see a colon
make sure you have FOUR spaces on all lines that go into the code block
"""

"""
but what does this IF statement do, its simple, it reads "if (this thing) is true, do the code underneath this line that 
is indented, we can close out of the statement but returning to the original indentation like this
"""

if truthy_num:
    print('this is the if statement code')
print('this is not')

"""
run this code and see what happens, and you should see 3 lines in your console
"""

"""
BUT WAIT THERE'S MORE, we can also check to see if something is NOT truthy
"""

if not truthy_num:
    print('this wont show up')
else:
    print('this will show up')

"""
the 'not' statement means we are checking to see if something is NOT true,
i also threw in the else statement, when we have an IF we can put in code that fires IF the statement isn't true,
else handles all other cases, its like having to pick between 2 doors, you can't go through both

run this code and see what we get
we only see 'this will show up' because truthy_num is true because it has value, so it does the else statement
"""

"""
now lets talk about booleans, booleans are actual True False values,
"""

bool_variable = True

if bool_variable:
    print('its true, chief')
elif not bool_variable:
    print('not sure about that one, chief')
else:
    print("I don't know about that one chief")

"""
this checks the literal True value of bool_variable
we also see the elif, this means ELSE IF,
elif is kinda like putting multiple IF's together. (note the same syntax)
it says if bool variable is not true, we are going to do this elif here, if that fails we'll do the else statement
you can have as many elif's as you can imagine
"""

# a value can also be NONE, or have NO VALUE. zero and none are different as zero HAS A VALUE

no_value_data = None

if no_value_data:
    print('it has value')
else:
    print('it has no value')

# if we run this we see that because no_value_data is None it is 'Falsey'
# therefore it runs the else statement
