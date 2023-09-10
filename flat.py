import numpy

array = numpy.array([
        [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 5, 1],
            [1, 2, 1, 5, 6],
            [1, 3, 3, 4, 1],
            [1, 3, 4, 1, 4],
            [1, 3, 4, 6, 1]
        ]
    ])

array = array.reshape(-1)
print(array)
