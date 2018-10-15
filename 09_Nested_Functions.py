
# Whenever we don't want to clutter up our code we can 'nest' our functions and loops
# this means we can put functions INSIDE of functions AND the function has access to the variables
# outside of the inner function


def get_colors():
    colors = ['red', 'blue', 'yellow']

    def get_colors_capitalized():
        capital_colors = []
        for color in colors:
            capital_colors.append(color.capitalize())
        return capital_colors
    colors = get_colors_capitalized()
    print(colors)


get_colors()

# this may look confusing but all we're doing is following the indents and making sure they align
# inside of our get_colors() method, we may need to capitalize the colors before printing them
# so we can just throw in that function inside and nest it

# the BIG reason we use this is because of something called a 'closure'
# a closure is an outside variable being referenced inside a nested function
# on line 8 we see we created a list called colors,
# and on line 12 we see that we are iterating through colors even tho we are in a different function
# but because they are nested its perfectly legal code to do it this way
