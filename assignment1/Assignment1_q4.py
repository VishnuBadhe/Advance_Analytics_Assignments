# Q.4 Replace all odd numbers in arr with -1
# 	Input:
# 	arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

import numpy as np

def function():
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr[arr % 2 == 1] = -1
    print(arr)

# function()

# OR

def function1():
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr[arr % 2 != 0] = -1
    print(arr)

# function1()

# OR

def function2():
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    for index in range(len(arr)):
        if index % 2 == 1:
            arr[index] = -1
        else:
            index += 1

    print(arr)

# function2()




# OR

def function3():
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    for index in range(len(arr)):
        if index % 2 != 0:
            arr[index] = -1
        else:
            index += 1

    print(arr)

# function3()










