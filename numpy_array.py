import numpy

array = numpy.array(
    [
        [[1, 2, 3, 4, 5], [11, 22, 33, 44, 55]],
        [[1, 1, 1, 1, 1], [ 2,  2,  2,  3,  3]],
        [[3, 3, 3, 3, 3], [ 3,  3,  3,  3,  4]]
    ])

print(array)
print(type(array))
print('dimension = ', array.ndim)

array2 = numpy.array([1, 2, 33, 4, 5], ndmin = 5)
print(array2)
