
# to explain yield, lets use our code from our last lesson,
# we had something that looks similar to this
# for student in f.readlines():

# but what does .readlines() do? well lets write our own function that does the same thing

students = []


def read_students(f):  # <-  f is the file we pass in just like our readlines() function
    for line in f:
        yield line  # <- wow what is this thing, well lets call it and see what happens


def read_file():
    try:
        f = open('10_Students.txt', 'r')
        for student in read_students(f):  # <- look how we call our new function here
            students.append(student)
        f.close()
    except Exception as e:
        print(e)


read_file()
print(students)

# if we run this we see it does the exact same thing as our readlines() function that's built in
# granted readlines() does more, but it works nonetheless

# so lets look at yield now, it is similar to 'return' but that returns one thing and goes back
# to the function it calls, yield can return multiple things
# that's because it allows us continue the method to completion, and return anything that fits our
# criteria, in this case its everything in our txt file
