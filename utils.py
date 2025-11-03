from random import randint

def get_radom_arrays(sizes):
    arrays = []
    for size in sizes:
        arrays.append([randint(0, 100) for _ in range(size)])
    return arrays

