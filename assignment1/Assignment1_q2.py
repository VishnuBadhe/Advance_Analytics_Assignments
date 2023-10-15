# Q.2 Create a 3×3 numpy array of all True’s

import numpy as np

def function():
    a1 = np.array([
        [True, True, True],
        [True, True, True],
        [True, True, True]
    ])
    print(f" 3 * 3 numpy array of all True values:\n {a1}")

function()

# OR

def function1():
    a2 = np.ones([3, 3], dtype=bool)
    print(f" 3 * 3 numpy array of all True values: {a2}")

# function1()