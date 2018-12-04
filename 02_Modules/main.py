
# in this lesson we are going to go over how we can use imports to split
# our python projects into 'modules'
# or more simply how we can make our files 'talk' to each other

# so i mentioned imports above so how do we do that, its pretty simple
# but there's different ways to do it, let's import our 2 other files, 2
# different ways

import student
from hs_student import HighSchoolStudent

# on line 12 we did a basic import, it means use this as the reference when
# we want to use anything in this file, that means we have to use student
# before we call our functions in another our student class we need to
# tell python that we are looking in another file

james = student.Student('james', 22)
# notices the new student prefix to our instantiation, this is because our
# import was not specific on what we are importing

# now lets see what happens when we use our high school student module

mike = HighSchoolStudent('mike', 9)
# we don't need to add the prefix, but why? that's because we used the from
# keyword and chose a specific part of the class to import
# the import on line 13 reads 'from this file, import this thing'
# we can also use an asterisk to mark 'all' members of the file like so

from hs_student import *

jenna = HighSchoolStudent('jenna', 8)

# we can also use the 'as' keyword to give a new name to what were importing
# lets see how that works

import student as stdt

jimmy = stdt.Student('jimmy', 55)
# now our module is named 'stdt'
# it reads 'import this thing and call it this'
