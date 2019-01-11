from main import *
from roulette_wheel import RuletteWheele

# seed_ = 100
#
# if seed_:
#     seed(seed_)

A = -1.0
B = 1.0
N_ = 4 # ilośc osobników
iter_x = 2 # ilość zmiennych
mut = 0.02
cros = 0.8
precision = 3
# losowanie populacji startowej
chromosome_length = chromosome_length(A,B, precision)



population = []
for i in range(0, N_):
    variables = []
    for j in range(0, iter_x):
        r = rand_precision_range(precision, A, B)
        variables.append(r)
    population.append(variables)



# ustalenie fitnessu

for i in population:
    fitness = fitness_rosenbrock(i)
    i.append(fitness)

print(population)
# zamiana na binarne
bin_population = []
for i in population:
    t = []

    for j in i[:iter_x]:
        t.append(to_binary(j, chromosome_length))
    b = connect_multi_variable(t)
    t = []
    t.append(b)
    t.append(i[-1])
    bin_population.append(t)


# Selekcja koło ruletki
r = RuletteWheele(bin_population)
after_rw = r.get_chosen()



#Krzyżowanie
after_crossover = []
c = []
for i in after_rw:
    r = random.random()
    if r <= cros:
        c.append(i[0])

# for l, i in enumerate(c):
#     while True:
#         r = random.randint(0, len(c))
#         if r != l:
#             pass


after_crossover = after_rw

#Mutacja
for i in after_crossover:
    r = random.random()
    if r <= mut:
        i = mutation(i)



#Rozdzielenie na pojedyncze chromosomy
split_population = []
for i in after_crossover:
    split_population.append(split_multi_variable(i, iter_x))


new_population =[]
for i in split_population:
    x = []
    for j in i:
        x.append(to_decimal(j, chromosome_length, precision))
    new_population.append(x)

print(" New Population")
print(new_population)







