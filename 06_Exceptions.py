
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


