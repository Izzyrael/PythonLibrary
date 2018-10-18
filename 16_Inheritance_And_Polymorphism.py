
# Inheritance is how we can create a 'parent-child' relationship with our classes
# imagine having a class that already has properties that we don't declare because they come from our 'parent' class
# python allows us to do this
# lets make an 'animal' class


class Animal:
    def speak(self):
        return "I'm an animal"


# but what is an animal? an animal is a group of mammals, fish, and other organisms. So lets dig down a little deeper


class Dog(Animal):  # notice how we added parenthesis to our class name... hmmm
    def __init__(self, name):
        self.name = name

    def get_greeting(self):
        return "my name is " + self.name


# when we add parenthesis to our class declaration(line 16) that means the class we are defining 'DERIVES' from
# what ever is in the parenthesis. that's alot of gibberish so lets see what it can do

dog = Dog('max')
print(dog.get_greeting())
print(dog.speak())

# but wait.. we don't have a 'speak()' function in dog? that's right! it's in our animal class. however our dog class
# derives from animal, so our dog class get ALL of our functions and attributes that animal has
# this is what a 'parent-child' or 'Base-sub' class relationship is
# we could also continue the chain and have classes that derive from 'Dog', but that's out of scope for now

# that is inheritance on a basic level, now lets talk about 'Polymorphism'
