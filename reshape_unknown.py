import numpy

array = numpy.array([12, 23, 34, 45, 56, 67, 78, 89, 93, 10, 11, 12])

array = array.reshape(3, 1, -1)
print(array)
