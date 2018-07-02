import numpy as np
import random
import math
import matplotlib.pyplot as plt


def weird_function(x):
    res = x * np.sin(10 * np.pi * x) + 2.0
    return res


def plot_start_function(x, y):
    line, = plt.plot(x, y, lw=2)
    plt.xlim(-1, 2)
    plt.show()

def decode_array(array, st):
    array = np.array(array)
    powers = np.arange(0, array.size,1)
    mult = np.array(array) * 2 ** powers
    sumation = np.sum(mult)
    x = (sumation / 2**array.size) * (st[1] - st[0]) + st[0]
    return x

def add_rec(list, tail_list):
    if list:
        second_pair = list[0]
        last_existing = tail_list[-1]
        new_pair = (last_existing[0] + second_pair[0], second_pair[1])
        tail_list.append(new_pair)
        if list[1:]:
            add_rec(list[1:],tail_list)
    return tail_list


