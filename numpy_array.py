import numpy

array = numpy.array(
    [
        [[1, 2, 3, 4, 5], [11, 22, 33, 44, 55]],
        [[1, 1, 1, 1, 1], [ 2, 12,  2,  3,  3]],
        [[3, 3, 3, 3, 3], [ 3,  3,  3,  3,  4]]
    ])

print(array)
print(type(array))
print('dimension = ', array.ndim)

array2 = numpy.array([1, 2, 33, 4, 5], ndmin = 5)
print(array2)

print("2nd element on 1st row is ", array[1, 1, 1])

print("Last element from 3rd dimension is ", array[2, 1, -2])

print("Array slice is ", array[2, 1, 1:5]);
