
# One cool feature in python is we can actually save and open information to/from Txt files
# python has built in functions to do this and we'll be going over that here

# let's write a couple of functions that will help us do this

students = []


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("10_Students.txt", "a")  # here's the open function. the 'a' means 'append to file'
        # if we didn't have the 'a' it would overwrite the entire file
        f.write(student + "\n")  # the '\n' is called an escape character, this one makes a new a line
        f.close()  # remember to close the file so we don't hog memory
    except Exception as e:
        print('could not read file', e)  # in case anything happens we do this


def read_file():
    try:
        f = open('10_Students.txt', 'r')  # the r means we're going to just read the file
        for student in f.readlines():
            add_student(student)  # 'reads the file and adds the students in the file to our python list
        f.close()
    except Exception as e:
        print('could not read file', e)


# Note: Writing and using dictionaries in a file can be pretty tricky and requires importing
# another module so we're just gonna create a list of names and write to that file
# we will get into modules and importing them later so don't worry


# now lets get into the code that uses the functions above
read_file()  # first we read the file to see all of the students already there
student_name = input('Enter name: ')  # now a couple of input statements to get user input
student_id = input('Enter ID: ')

# and now we call our function add_student() because we have the information from our user
add_student(student_name, student_id)
save_file(student_name)  # and save the file, every time we open this file we will have our students saved

# give it a run and see what happens when you enter a student, and re run your code
