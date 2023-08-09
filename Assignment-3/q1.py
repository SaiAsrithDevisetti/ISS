from __future__ import print_function
val = int(input("Enter the length of stars: "))
value = int(val/2)

for i in range(value):
    for j in range(i):
        print(' ', end='')
    for j in range(val - (2*i)):
        print('*', end='')
    for j in range(i):
        print(' ', end='')
    print()

for i in range(value):
    for j in range(value - 1 - i):
        print(' ', end='')
    for j in range(val - (2 * (value - 1 - i))):
        print('*', end='')
    for j in range(value - 1 - i):
        print(' ', end='')
    print()
