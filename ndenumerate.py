import numpy

array = numpy.random.randint(27, size = (3, 3, 3))
print(array)

for id, n in numpy.ndenumerate(array):
    print(id, n)
