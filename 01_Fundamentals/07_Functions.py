
# functions are the 'verbs' of our programs
# it is a block of organized and reusable code that performs a certain function
# you should try to make your function do one thing and usually no more
# we've already seen print(), print is a function. it prints something to the screen

# to write a function we first need a new keyword, 'def'
# 'def' means we are 'defining' a function

students = []


def add_student(name):
    students.append(name)


# notice the parenthesis before the colon, this is what we 'give' our function
# we can have as many variables (or lack there of) as we want in there, they are called parameters
# so whenever we do add_student() and give it a name, it will add that name to our list
# lets try it

add_student('billy')
print(students)

# we can also pass in a variable instead of a hard coded string

first_name = 'billy'
add_student(first_name)
print(students)

# now we see billy twice if we run this
# remember the parameters have to match, we can't only give our function 1 variable if we have
# 2 parameters where we define it

# now we're going to look at 'return' statements

add_student('jimmy')


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student.title())
    return students_titlecase  # the return means 'give this value back to whoever called the function


# this means if we call the function get_students_titlecase() and assign it to a new variable
# the RETURN will be the value assigned to the new variable

student_list = get_students_titlecase()

print(student_list)

# Complete Challenge 7
