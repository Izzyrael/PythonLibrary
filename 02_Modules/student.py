
# Student class for main.py


class Student:

    school_name = 'Springfield Elementary'

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name
