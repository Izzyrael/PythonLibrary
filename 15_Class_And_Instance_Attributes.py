
# For this lesson we're are going to need to bring back our class from the last lesson
# with a few key add ons necessary to explain, consider the following code

students = []


class Student:
    def __init__(self, name, student_id):
        self.name = name  # <- Notice how we are creating variables here,
        self.student_id = student_id  # <- these allow us to get rid our dictionary
        # these variables will be in every single student object we create now
        # AND we don't have a dictionary anymore so everything is more accessible
        students.append(self)  # this means append 'THIS INSTANCE' to our list above

    def __str__(self):
        return '{0} {1}'.format(self.name, self.student_id)
        # here we want to return the variables of our student instance, so we can
        # use the variables inside of our return statement so every instance is unique
        # remember to use 'self' again

    def get_name_capitalized(self):  # our new method that takes in this instance
        return self.name.capitalize()  # and takes the variable 'name' created above
        # and capitalizes it, remember we need self so it knows we are talking about
        # 'THIS' student, not another one, it is referring to 'ITS SELF'


mark = Student('mark', 5)
marks_name = mark.get_name_capitalized()

print(mark)
print(marks_name)

# This is a lot of code, and a lot of comments, but that's fine, take a minute to
# disect and figure out what's going on when we create a new student

# OK so now that we see the many uses of 'INSTANCE' attributes, let's dive into 'CLASS' attributes
# instance attributes will always be marked with 'self' that means they are available to all instances
# but what if we only have 1 school? consider the following code


class School:
    school_name = 'a good school'
    school_address = '321 good lane'


# this is still a class, however we don't see any constructors or generator methods (such as __str__)
# now check this out

print(School.school_name)
# THIS WORKS, but we never made an instance of 'School' (school = School()), that's weird
# that's because these are 'STATIC' 'CLASS' Attributes, in other words, we only have 1 school
# when something is static we don't need to create an instance, we WILL cover that later on so don't worry
# if that's too much right now, just remember why we use 'self'
