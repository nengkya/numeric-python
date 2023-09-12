import numpy

array1 = numpy.arange(36).reshape(3, 4, 3)
array2 = numpy.random.randint(44, size=(3, 4, 3))
#print(array1)
#print(array2)

array = numpy.concatenate((array1, array2), axis = 0)
print(array)
print('----------------------------------------')
array = numpy.stack((array1, array2), axis = 1)
print(array)
