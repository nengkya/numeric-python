import numpy

array = numpy.arange(16).reshape(2, 2, 4)

for n in numpy.nditer(array):
    print(n)
