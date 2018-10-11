
"""
Remember that I said we're going to be talking about other collections?
Get ready for dictionaries
a dictionary is different from a list because it forms a 'KeyValue Pair',
heres an example
"""

student = {  # the left hand side is our Key, and the right hand side is our Value, hence KeyValue
    'name': 'mark',
    'student_id': 1,
    'feedback': None
}

# dictionaries are very useful for storing structured Data
# to merge dictionaries we can simply create a list of dictionaries

all_students = [
    {'name': 'mark', 'student_id': 1},
    {'name': 'jenna', 'student_id': 2},
    {'name': 'jill', 'student_id': 3}
]

# but how do we get 'just the name'?

# WE USE THE KEY
# lets use our student dictionary from earlier..

name = student['name']
print(name)

# run this and we get 'mark'
# that's because we are giving our dictionary the 'Key' and it gives us the 'Value' stored under that key
# pretty nifty right?
