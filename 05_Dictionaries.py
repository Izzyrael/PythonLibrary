
"""
Remember that I said we're going to be talking about other collections?
Get ready for dictionaries
a dictionary is different from a list because it forms a 'KeyValue Pair',
here's an example
"""
#          Key     Value
student = {'name': 'mark', 'student_id': 1, 'feedback': None}

# we can also write our dictionaries like this to make it easier to read
student = {  # the left hand side is our Key, and the right hand side is our Value, hence KeyValue
    'name': 'mark',
    'student_id': 1,
    'feedback': None
}

# if you have prior programming knowledge this looks pretty similar to JSON (javascript object notation)
# dictionaries are very useful for storing structured Data
# to merge dictionaries we can simply create a list of dictionaries

all_students = [
    {
        'name': 'mark',
        'student_id': 1
    },
    {
        'name': 'jenna',
        'student_id': 2
    },
    {
        'name': 'jill',
        'student_id': 3
    }
]

# but how do we get 'just the name'?

# WE USE THE KEY
# lets use our student dictionary from earlier..

name = student['name']
print(name)

# run this and we get 'mark'
# that's because we are giving our dictionary the 'Key' and it gives us the 'Value' stored under that key
# pretty nifty right?

# but what if we want to get ALL of the students name's
# that's where the placeholders come in handy
for student in all_students:
    print(student['name'])

# this code says for each student in all_students, store the element its looping over in student
# that way we have access to the student's name
# when it loops back after completing the print, student becomes the next student dictionary
# we call this an 'object', a student has multiple things in it and can be manipulated

all_students[0]['name'] = 'jimbo'
print(all_students[0]['name'])

# see? we can manipulate data INSIDE of a student OBJECT
