from math import sqrt

def to_circular(x):
    largest_square = 0
    for i in range(1, int(sqrt(x))):
        if x - i**2 > 0:
            largest_square = i

    print(largest_square)


to_circular(25)
to_circular(1)
to_circular(10)