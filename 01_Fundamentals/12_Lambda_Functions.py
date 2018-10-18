
# lambda functions are anonymous functions that allow us to write short and simple functions
# they can take arguments and get called the same way as a normal function
# so what if we want a function that doubles a number, lets do that now
# anonymous means nameless, we can use them if we need a function for a short period of time
# that kind of 'helps' our code


def double(x):
    return x * 2


# easy right? lets make it even simpler


doubled_number = lambda x: x * 2  # notice no parenthesis and the new 'lambda' keyword

# and then to call it we do this
print(doubled_number(5))


# useful in higher order functions, or function that take functions as arguments, so instead of
# writing out an entire function we can just give it a lambda

# here's an example of that

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

even_list = list(filter(lambda x: (x % 2 == 0), my_list))

print(even_list)
