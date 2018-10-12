
# in this lesson we are going to go over parameters/arguments
# we're going to need our functions from our last lesson so lets write them out now

students = []


def add_student(name):
    students.append(name)


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase


# but what if we want to make an argument optional, or not required
# its easy! lets write a new function that will also assign an id to a student

def add_student_with_id(name, student_id=332):  # note the =332
    student = {'name': name, 'student_id': student_id}  # here's another dictionary, these are very useful
    students.append(student)


# on line 22 we see that we have set student_id to a hardcoded value of 332
# this way we don't need to supply our function call with a student_id
# lets see what that looks like

add_student_with_id('connor')
print(students)

# if we run this we see that it works, even though our function looks like it wants a value for student_id
# however we can also manually give it a value if we would like

add_student_with_id('bill', 1)
print(students)

# if we run this we see that the value of 332 gets overridden by the value we gave when we called the function
# we can actually do some pretty nifty stuff with our print function with arguments
# try and figure this out

print('hello', 'world', 3, None, 'something')

# this is because the print function uses 'variable' arguments
# basically it means that the parameters can 'vary' and don't have a set limit
# lets dig into it


def variable_arguments(name, *args):  # notice the asterisk
    print(name)
    print(args)  # no asterisk here


variable_arguments('Jimmothy', None, 'Python is cool')
# run this and see what happens
# we see it captured our first argument and stored it in name, and printed it
# then all of our other arguments get printed 2cnd
# also notice that it placed the other arguments in a list
# we can have as many arguments as we want now

# now lets get into keyword arguments, what if we want to specify what the argument was?
# in the last example we see that its just a big ole' list
# we can use keyword arguments to convert it into a dictionary so we can sift through
# key value pairs where the keys are the names of the arguments


def keyword_args(name, **kwargs):  # notice the double * and KWargs (key word args)
    print(name)
    print(kwargs['description'], kwargs['type'])


keyword_args('connor', description='a funny dude', type='person')
# notice the red, it picked up that those words were part of the function
# run this and see what happens

# it replaces the kwargs['something in here'] with what we give it

# SIDE BAR:
# what if we want the user to input data...
# there's a built in function for that, its called 'input'

input_student_id = input('Enter student ID: ')
input_student_name = input('Enter student name: ')
# these functions will print whats in the parenthesis, and when we press enter it will take the
# string that A USER enter through the console and store them in the variable to the left
# so wait... that means we can use those variables in our functions

add_student_with_id(input_student_name, input_student_id)
print(students)
