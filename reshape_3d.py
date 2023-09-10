import numpy as np

array = np.array([17, 22, 36, 47, 53, 65, 57, 82, 94, 10, 12, 11])

array = array.reshape(3, 2, 2)

for iterate_3d in array:
    for iterate_2d in iterate_3d:
        print('------------')
        print(iterate_2d)
