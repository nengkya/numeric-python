import numpy

array = numpy.array(
    [
        [[ 1,  2,  3, 4,  5], [11, 22, 33, 44, 55]],
        [[ 1,  1,  1, 1,  1], [ 2, 12,  2, 31,  3]],
        [[13, 37, 32, 3, 23], [ 3,  3,  3,  3,  4]]
    ])

print(array)
print(type(array))
print('dimension = ', array.ndim)

array2 = numpy.array([1, 2, 33, 4, 5], ndmin = 5)
print(array2)

print('2nd element on 2nd row array[1, 1, 1] is', array[1, 1, 1])

print('Last element from 3rd dimension is', array[2, 1, -2])

print('Array slice range array[2, 1, 1:4] is', array[2, 1, 1:4]);

print('Slice from middle to end array[0, 1, 2:] is', array[0, 1, 2:])

print('Slice from the beginning to point array[2, 1, :4] is', array[2, 1, :4])

print('Slice negative backward array[1, 1, -3:-1] is', array[1, 1, -3:-1]);
