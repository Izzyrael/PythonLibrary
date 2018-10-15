
# now lets get into something we call 'classes'
# classes, are similar to functions but are kind of like 'blueprints'
# they typically have more than one function, variables, and uses
# kind of like our dictionary we were using for students, lets make a student 'class'

students = []


class Student:
    def add_student(self, name, student_id=332):  # <- notice the self keyword more on that below
        student = {'name': name, "student_id": student_id}
        students.append(student)

# so now that we have a class defined we need to create an 'instance' of the class
# that's a weird word, what does it mean?
# basically it means we need to use our blueprint (the class) and make something with it
# these instances will be completely separate from other instances, for example


student = Student()
lilly = Student

# student is a student and lilly is a student, they are both INSTANCES of the student class
# but are different from each other, lilly will have a different Id, different grades, etc, from student

# now that we have some instances, we can use the functions in our classes
student.add_student('Mark')
print(students)

# run this and see what happens
# we can have as many functions in our classes, buts its best practice to keep it relevant to the class

# on 'SELF': the self keyword refers to 'this' class we are working on, or this INSTANCE of the class
# it's how we refer to the class, from the class (kinda like the word mySELF)
