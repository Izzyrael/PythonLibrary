
"""
Exceptions are errors that stop the program from running entirely
This lesson we're going to learn Exception Handling by using Try Except blocks
"""

# lets make a new student dict like we did in the last lesson
student = {
    'name': 'Connor',
    'student_id': 1,
    'courses': [
        {'name': 'english'},
        {'name': 'math'},
        {'name': 'science'}
    ]
}
# THIS MAY LOOK CONFUSING BUT ITS SIMPLE, we are putting a dictionary INSIDE another dictionary :D
# i hope that's an aha moment

# last time if we searched for a Key that didn't exist, it gave us a KeyError exception and stopped the program
# now lets put it in a try block
# a 'Try Except' blocks read 'try this code and attempt to run it, 'except' when an error occurs'
# pretty simple
try:
    last_name = student['last_name']
except KeyError:
    print('no key found')
print('but it still works')

# if we run this we see that we have no key of 'last_name' but the code still runs, and it finishes the program
# this is basic exception handling if we know our code may break, we can 'catch' those exceptions and do something else

# this may seem pretty stupid, but it has uses. later on when write to files, if we don't have permission to write to
# said file, it'll throw an exception and break the execution. instead we can say 'you don't have permission
#   to access this file'

# there are many different types of exceptions in python and we'll cover a few here to get familiar
# one other exception is a 'TypeError' exception, this happens when you try to manipulate 2 different data types

# lets add our last_name key value pair
# we can do this like so

student['last_name'] = 'Mullett'

# now lets write some new code to demonstrate

# print('string' + 1)
# this will throw a type error and it is why it is commented out, uncomment and run it to see the error

# back to our student example lets catch the type error and handle it

try:
    last_name = student['last_name']
    numbered_last_name = 3 + last_name
except TypeError:
    print('Type Error Occurred')
print('but it still works')

# run this to see what our code does
# we see that it printed TypeError occurred

# we can also have many different 'except' statements like this

try:
    last_name = student['last_name']
    numbered_last_name = 3 + last_name
except TypeError:
    print('Type Error Occurred')
except KeyError:
    print('Key Error Occurred')
print('but it still works')

# if we don't know what exception will occur but still want to catch it we can use Exception
# or it will catch ALL exceptions

try:
    number = 3 + 'division'
except Exception:
    print('Unknown Error')


