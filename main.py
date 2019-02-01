# import random
# from random import seed
# import textwrap
# import itertools
#
# import numpy as np
#
#
# # def chromosome_length(A, B, precision):
# #     abs_ = (abs(A) + abs(B))
# #     small_sectors = abs_ * pow(10, precision)
# #     for i in itertools.count():
# #         if pow(2, i) < small_sectors < pow(2, i + 1):
# #             return i + 1
#
#
# # def to_binary(d, chromosome_length):
# #     binary = ((d + 1.0) * (pow(2, chromosome_length) - 1)) / 3
# #     return bin(int(binary))[2:].zfill(chromosome_length)
# #
# #
# # def to_decimal(b, chromosome_length, precision):
# #     binary = int(b, 2)
# #     x = -1.0 + (3 * binary) / (pow(2, chromosome_length) - 1)
# #     return round(x, precision)
# #
# #
# # def split_multi_variable(string, number_of_variables):
# #     parts = len(string) / number_of_variables
# #     return textwrap.wrap(string, int(parts))
#
#
# # def connect_multi_variable(strings):
# #     string = ""
# #     for i in strings:
# #         string = string + i
# #     return string
#
#
# # def rand_precision_range(precision, A, B):
# #     return round(random.uniform(A, B), precision)
#
#
# # def sphere(x):
# #     suma = 0
# #     for i in x:
# #         suma = suma + pow(i, 2)
# #     return suma
# #
# #
# # def fitness_sphere(x):
# #     suma = 0
# #     for i in x:
# #         suma = suma + pow(i, 2)
# #     if suma == 0:
# #         return 0
# #     else:
# #         return 1 / suma
# #
# #
# # def rosenbrock(x):
# #     suma = 0
# #     for i in range(0, len(x) - 1):
# #         suma = suma + 100.0 * (x[i + 1] - x[i] ** 2.0) ** 2.0 + (1 - x[i]) ** 2.0
# #     return suma
# #
# #
# # def fitness_rosenbrock(x):
# #     suma = 0
# #     for i in range(0, len(x) - 1):
# #         suma = suma + 100.0 * (x[i + 1] - x[i] ** 2.0) ** 2.0 + (1 - x[i]) ** 2.0
# #     if suma == 0:
# #         return 0
# #     else:
# #         return 1 / suma
# #
# #
# # def shekels_foxholes(x):
# #     a_ij = [[-32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32]
# #             [-32, -32, -32, -32, -32, -16, -16, -16, -16, -16, 0, 0, 0, 0, 0, 16, 16, 16, 16, 16, 32, 32, 32, 32, 32]]
# #     # https://al-roomi.org/benchmarks/unconstrained/2-dimensions/7-shekel-s-foxholes-function
# #     suma = 1 / 500
# #     for i in range(1, 25):
# #         pass
# #
# #
# # def fitness_foxholes(x):
# #     pass
#
#
# # def mutation(chromosome, seed_=None):
# #     r = random.randint(0, len(chromosome) - 1)
# #     binary = list(chromosome)
# #
# #     if binary[r] == "1":
# #         binary[r] = "0"
# #     else:
# #         binary[r] = "1"
# #
# #     binary = "".join(binary)
# #
# #     return binary
# #
# #
# # def crossover(chromosome1, chromosome2, seed_=None):
# #     r = random.randint(0, len(chromosome1) - 1)
# #
# #     o1 = chromosome1[:r] + chromosome2[r:]
# #     o2 = chromosome2[:r] + chromosome1[r:]
# #
# #     return [o1, o2]
#
# # A = -1
# # B = 2
# # chromosome = "1000101110110101000111"
# # precision = 6  # (10^-6)
# # chromosome_length = chromosome_length(A, B, precision)
# # chromosome_prim = int(chromosome)
# # number_of_variables = 4
# #
# #
# # ch = []
# # for i in range(0, 4):
# #     ch.append(rand_precision_range(precision, A,B))
# #     print(ch[i])
# #
# # ch_bin = []
# # for i in ch:
# #     ch_bin.append(to_binary(i))
# #
# # print(connect_multi_variable(ch_bin))
# # print(split_multi_variable(connect_multi_variable(ch_bin)))
# #
# # for i in split_multi_variable(connect_multi_variable(ch_bin)):
# #     print(to_decimal(i))
# #
# #
# # print(to_binary(-0.63719))
# # print(to_decimal(to_binary(-0.63719)))
# #
# # print(fitness_rosenbrock([10,20,30]))
# from Conversion import *
# from Genetic_Operator import *
# A = -1.0
# B = 1.0
# N_ = 500 # ilośc osobników
# iter_x = 2  # ilość zmiennych
# mut = 0.02
# cros = 0.8
# precision = 3
#
# population = []
# for i in range(0, N_):
#     variables = []
#     for j in range(0, iter_x):
#         r = Conversion.rand_precision_range(precision, A, B)
#         variables.append(r)
#     population.append(variables)
#
# print(population)
# # Krzyżowanie
# after_rw = population
# after_crossover = []
# c = []
# for i in after_rw:
#     r = random.random()
#     if r <= cros:
#         c.append(i)
#
# if len(c) < N_:
#     # print("Długość N: ", N_)
#     # print("Długość przed: ", len(c))
#     for i in range(0, (N_ - len(c))):
#         r = random.randint(0, len(c)-1)
#         c.append(c[r])
#     # print("Długość po: ", len(c))
#
# unpaired = False
# if len(c) % 2 != 0:  # musi być parzyscie do krzyżowania
#     c.append(c[0])
#     unpaired = True
#
#
# A = c[:len(c) // 2]
# B = c[len(c) // 2:]
#
# for i in range(0, len(A)):
#     o1, o2 = GeneticOperator.crossover(A[i], B[i])
#     after_crossover.append(o1)
#     after_crossover.append(o2)
#
# if unpaired:  # Do krzyżowania jest potrzerbna parzysta liczba osobników, ale nie może być ich po krzyżowaniu więcej niż N_ więc usuwamy ostatniego
#     print("Przed: ", after_crossover)
#     del after_crossover[-1]
#     print("Po: ", after_crossover)
#     unpaired = False
# # print("Krzyżowanie ", after_crossover)
import random

import numpy as np
import ctypes
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from GUI import *

if __name__ == '__main__':
    user32 = ctypes.windll.user32
    user32 = ctypes.windll.user32
    szerokosc = user32.GetSystemMetrics(0) - 150
    wysokosc = user32.GetSystemMetrics(1) - 200
    app = QApplication(sys.argv)
    main = Window()
    main.setWindowTitle("Optymalizacja funkcji wielu zmiennych za pomocą algorytmu genetycznego")
    main.setGeometry(user32.GetSystemMetrics(0) / 2 - szerokosc / 2, user32.GetSystemMetrics(1) / 2 - wysokosc / 2,
                     szerokosc, wysokosc)
    main.show()
    sys.exit(app.exec_())


# from Genetic_Operator import GeneticOperator
# c = []
# cros = 0.8
# after_crossover = []
# population = ['1234', '5678', '1111', '0000', '9999']
# print("Przed krzyżowanie ", population)
# for i in population:
#     r = random.random()
#     if r <= cros:
#         c.append(i)
# print("Doszło 0")
# print(c)
# if len(c) < len(population):
#     print("Weszło")
#     # print("Długość N: ", N_)
#     # print("Długość przed: ", len(c))
#     for i in range((len(population) - len(c))):
#         r = random.randint(0, len(c) - 1)
#
#         c.append(c[r])
#     # print("Długość po: ", len(c))
# print("Doszło 1")
# print(len(c))
# unpaired = False
# if len(c) % 2 != 0:  # musi być parzyscie do krzyżowania
#     c.append(c[0])
#     unpaired = True
#
# # half = int(len(c)/2)
# # print(half)
# # ax = c[:half]
# # ay = c[half:]
# print(len(c) // 2)
# ax = c[:len(c) // 2]
# ay = c[len(c) // 2:]
# print(ax)
# print(ay)
# print("Doszło 2")
# for i in range(0, len(ax)):
#     o1, o2 = GeneticOperator.crossover(ax[i], ay[i])
#     after_crossover.append(o1)
#     after_crossover.append(o2)
# print("Doszło 3")
# if unpaired:  # Do krzyżowania jest potrzerbna parzysta liczba osobników, ale nie może być ich po krzyżowaniu więcej niż N_ więc usuwamy ostatniego
#     # print("Przed: ", after_crossover)
#     del after_crossover[-1]
#     # print("Po: ", after_crossover)
#     unpaired = False
# # print("Krzyżowanie ", after_crossover)
#
# population = after_crossover
# print("Po krzyżowaniu ", population)
