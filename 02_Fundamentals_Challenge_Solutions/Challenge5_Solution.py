
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for i in my_dict:

    if my_dict[i] % 2 == 0:
        my_dict[i] = 0

print(my_dict)
