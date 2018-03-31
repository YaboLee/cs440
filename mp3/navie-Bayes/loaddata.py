import numpy as np
import pandas as pd
from Digit import *


# f = open("../digitdata/optdigits-orig_test.txt")
# lines = f.readlines()
#
# for i in range(32, len(lines), 33):
#     # print(i)
#     print(lines[i])

def load_training(filename="../digitdata/optdigits-orig_test.txt"):
    '''
        Load training data;
        return a dictionary of objects, digits class
    '''
    f = open(filename)
    lines = f.readlines()

    digit_dict = {}
    for i in range(0, 10):
        digit_dict[i] = Digit(i)

    for i in range(32, len(lines), 33):
        image = lines[i-32:i]
        digit_dict[int(lines[i])].add_token(image)

    return digit_dict
