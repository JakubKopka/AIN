import itertools
import random
import textwrap

import numpy as np


class Conversion:

    @staticmethod
    def to_binary(d, A, B, chromosome_length):
        b = ((d * (pow(2, chromosome_length)) - (A * (pow(2, chromosome_length))))) / (B - A)
        return bin(int(b)).replace("0b", "").zfill(chromosome_length)

    @staticmethod
    def to_decimal(b, A, B, chromosome_length, precision):
        binary = int(b, 2)
        x = ((B-A) * binary) / (pow(2, chromosome_length) - 1) + A
        return round(x, precision)

    @staticmethod
    def split_multi_variable(string, number_of_variables):
        parts = len(string) / number_of_variables
        return textwrap.wrap(string, int(parts))

    @staticmethod
    def connect_multi_variable(strings):
        string = ""
        for i in strings:
            string = string + i
        return string

    @staticmethod
    def rand_precision_range(precision, A, B):
        return round(random.uniform(A, B), precision)

    @staticmethod
    def variable_length(A, B, precision):
        if A <= 0:
            abs_ = (abs(A) + abs(B))
        else:
            abs_ = B - A
        small_sectors = abs_ * pow(10, precision)
        for i in itertools.count():
            if pow(2, i) < small_sectors < pow(2, i + 1):
                return i + 1


# A = -2.0
# B = 2.5
# precision = 3
# losowanie populacji startowej


# print("x", Conversion.to_binary(-5.5, 13))
# print("y", np.binary_repr(5, 13))
#
# def bindigits(n, bits):
#     s = bin(n & int("1"*bits, 2))[2:]
#     return ("{0:0>%s}" % (bits)).format(s)
#
# print(bindigits(-3, 4))
#
# print(bin(-5))
# print(int("-0b101", 2))

# print(Conversion.to_binary(-2.348, -2, 2.5, 13))
#
# print(Conversion.to_decimal("1111011101011", -2, 2.5, 13, 3))
