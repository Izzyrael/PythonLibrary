
# remember our syntax for creating instances?
# student = Student()
# what does 'Student()' mean? its a constructor!
# constructors are methods (similar to functions), that run when an instance is created
# by default it is hidden, we can have more than one, and we can write our own
# lets rewrite our student class but make it simpler with constructors

students = []


class Student:
    def __init__(self, name, student_id):  # <- __int__ is our constructor name
        # 2 underscores
        student = {'name': name, 'student_id': student_id}
        students.append(student)


new_student = Student('bill', 3)  # we put the parameters here, instead of calling add_student()
# this allows us to make it simpler, and execute something on 'instantiation'
# or when we create an instance, same thing
print(students)

# but what if we want to print our object... lets try it
print(new_student)  # <- run this and see what happens
# we get __main__.Student object at 0x0369FDD0
# this code at the end is the memory address for our student object
# but we don't want that, we can use something called an 'override' method
# lets make a new class and do that


class Animal:
    def __str__(self):
        return "It's an animal"


# now lets create an animal instance and try and print it
animal = Animal()
print(animal)  # <- run this
# we get 'it's an animal' as an output
# this is because we over rid the '__str__()'method (the tostring() method)
# so instead of giving us the default memory location we can get something else
# more on this in later lessons
