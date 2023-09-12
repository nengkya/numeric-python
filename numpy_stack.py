import numpy

random = numpy.random.randint(16, size = (2, 2, 2, 2))
arange = numpy.arange(16).reshape(2, 2, 2, 2)
print(random)
print('-------------')
print(arange)
print('-------------')
stack = numpy.stack((random, arange), axis = 1)
print(stack)
