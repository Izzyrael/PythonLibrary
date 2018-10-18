
counter = 0

for i in range(1000):
    if counter == 100:
        print(i)
        counter = 0
    counter = counter + 1

print('done')
