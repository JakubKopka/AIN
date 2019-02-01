from Genetic_Operator import *
from Conversion import *
from Functions_and_Fittnes import FunctionsAndFittnes
from Tournament_Selection import TournamentSelection
from main import *
from Roulette_Wheel import *

seed_ = None

if seed_:
    seed(seed_)

#TODO
# 1) Nie działa dla ilości zmiennych == 1
# 2) Napisać funkcję lise jamy


A = -2
B = 2
N_ = 100 #ilośc osobników
iter_x = 2  # ilość zmiennych
generators_number = 100
mut = 0.01
cros = 0.8
precision = 5
# losowanie populacji startowej
chromosome_length = Conversion.variable_length(A, B, precision)
print("dlugosc osobnika: ", chromosome_length)

population = []
for i in range(N_):
    variables = []
    for j in range(0, iter_x):
        r = Conversion.rand_precision_range(precision, A, B)
        variables.append(r)
    population.append(variables)
print(population)
# ustalenie fitnessu
licznik = 1
average = []
best = []

def get_average_rosenborck(population):
    suma = 0
    for i in population:
        suma = suma + FunctionsAndFittnes.rosenbrock(i)
    avg = suma / len(population)
    average.append(avg)
    return avg


while licznik < generators_number:
    for i in population:
        fitness = 1/FunctionsAndFittnes.rosenbrock(i)
        if fitness < 0:
            print(i)
            print("---------------------------------------")
        i.append(fitness)

    # print(population)
    # zamiana na binarne
    bin_population = []
    for i in population:
        t = []

        for j in i[:iter_x]:
            t.append(Conversion.to_binary(j, A,B, chromosome_length))
        b = Conversion.connect_multi_variable(t)
        t = []
        t.append(b)
        t.append(i[-1])
        bin_population.append(t)

    # Selekcja koło ruletki
    r = RuletteWheele(bin_population)
    after_rw = r.get_chosen()

    #Selekcja turniejowa
    # k = 2
    # ts = TournamentSelection(bin_population, k)
    # after_ts = ts.tournament()
    # after_rw = after_ts
    # Krzyżowanie
    after_crossover = []
    c = []
    for i in after_rw:
        r = random.random()
        if r <= cros:
            c.append(i)

    if len(c) < N_:
        # print("Długość N: ", N_)
        # print("Długość przed: ", len(c))
        for i in range(0, (N_ - len(c))):
            r = random.randint(0, len(c) - 1)
            c.append(c[r])
        # print("Długość po: ", len(c))

    unpaired = False
    if len(c) % 2 != 0:  # musi być parzyscie do krzyżowania
        c.append(c[0])
        unpaired = True

    ax = c[:len(c) // 2]
    ay = c[len(c) // 2:]

    for i in range(0, len(ax)):
        o1, o2 = GeneticOperator.crossover(ax[i], ay[i])
        after_crossover.append(o1)
        after_crossover.append(o2)

    if unpaired:  # Do krzyżowania jest potrzerbna parzysta liczba osobników, ale nie może być ich po krzyżowaniu więcej niż N_ więc usuwamy ostatniego
        # print("Przed: ", after_crossover)
        del after_crossover[-1]
        # print("Po: ", after_crossover)
        unpaired = False
    # print("Krzyżowanie ", after_crossover)

    # Mutacja
    for i in after_crossover:
        # r = random.random()
        # if r <= mut:
        i = GeneticOperator.mutation(i, mut)

    # Rozdzielenie na pojedyncze chromosomy
    split_population = []
    for i in after_crossover:
        split_population.append(Conversion.split_multi_variable(i, iter_x))

    new_population = []
    for i in split_population:
        x = []
        for j in i:
            x.append(Conversion.to_decimal(j, A, B, chromosome_length, precision))
        new_population.append(x)



        ########################################################################################################





    pop = []
    min_ = []
    for i in new_population:
        r = FunctionsAndFittnes.rosenbrock(i)
        min_.append(r)
        pop.append(r)
    print(licznik, " Min:", min(min_), " Max:", max(min_))
    best.append(min(min_))

    print("Avarege of population: ", get_average_rosenborck(new_population))
    licznik = licznik + 1


print(" New Population")
# print(new_population)
# print(len(new_population))

maxx = []
for i in new_population:
    r = FunctionsAndFittnes.rosenbrock(i)
    maxx.append(r)
    i.append(r)

print(new_population)



for i in new_population:
    if i[-1] == min(maxx):
        print("x1:", i[0], " x2:", i[1], " f(x1,x2)=", i[-1])

import matplotlib.pyplot as plt
iterators = list(range(1, len(average)+1))
plt.plot(list(range(1, len(average)+1)),  average,list(range(1, len(best)+1)), best )
plt.ylabel('some numbers')
plt.show()


print(best)