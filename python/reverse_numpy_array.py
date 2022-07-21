import numpy


def arrays(arr):
    # complete this function
    # use numpy.array
    # reverse the array
    return numpy.array(arr[::-1], dtype=numpy.float64)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
