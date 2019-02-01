import random

from Conversion import *
from Functions_and_Fittnes import FunctionsAndFittnes
from Genetic_Operator import GeneticOperator
from Roulette_Wheel import RuletteWheele
from Tournament_Selection import TournamentSelection


class GeneticAlgorithm:
    average = []
    best = []

    def __init__(self, population, generation_number, selection_type, precision, cros, mut, function, n, interval,
                 seed_):
        print("Doszło #000000")
        self.popu = population
        self.generation_number = generation_number
        self.selection_type = selection_type
        print("selection_type", selection_type)
        self.precision = precision
        self.cros = cros
        self.mut = mut
        self.function = function
        print ("f:",function)
        self.n = n
        interval = interval.split(';')
        self.A = float(interval[0])
        self.B = float(interval[1])
        self.seed = int(seed_)
        if self.seed != -1:
            random.seed(self.seed)

        self.chromosome_length = Conversion.variable_length(self.A, self.B, self.precision)
        self.start()

    def get_best(self):
        return self.best

    def get_average(self):
        return self.average

    def start(self):
        self.population = self.create_populations()
        print("self population ", self.population)
        licznik = 0
        while licznik < self.generation_number:
            print("Doszło #2")

            # Tworzenie Fitnesu
            self.create_fitness()
            print("Doszło #3")
            # Zamiana na binarne
            self.toBinary()
            print("Doszło #4")
            # Selekcja
            if self.selection_type == 0:
                # Koło ruletki
                self.rulette_wheele()
            elif self.selection_type == 1:
                # Turniejowa
                self.tournament_selection(2)
            elif self.selection_type == 2:
                # Turniejowa
                self.tournament_selection(3)
            elif self.selection_type == 3:
                # Turniejowa
                self.tournament_selection(4)
            elif self.selection_type == 4:
                # Turniejowa
                self.tournament_selection(5)

            # Krzyżowanie
            self.crossover()
            print("Doszło #6")
            # Rozłącz na pojedyńcze punkty
            self.split_chromosome()
            print("Doszło #7")
            print(licznik, " - ", self.population)
            licznik = licznik + 1
            self.get_best()
            self.get_average(0)

    def get_best(self):
        min_ = []
        for i in self.population:
            r = FunctionsAndFittnes.rosenbrock(i)
            min_.append(r)

        self.best.append(min(min_))

    def get_average(self, number_of_function):
        suma = 0
        for i in self.population:
            if number_of_function == 0:
                suma = suma + FunctionsAndFittnes.rosenbrock(i)
            elif number_of_function == 1:
                suma = suma + FunctionsAndFittnes.sphere(i)
            elif number_of_function == 2:
                suma = suma + FunctionsAndFittnes.shekels_foxholes(i, self.n)
        avg = suma / len(self.population)
        self.average.append(avg)

    def split_chromosome(self):
        split_population = []
        for i in self.population:
            split_population.append(Conversion.split_multi_variable(i, self.n))

        new_population = []
        for i in split_population:
            x = []
            for j in i:
                x.append(Conversion.to_decimal(j, self.A, self.B, self.chromosome_length, self.precision))
            new_population.append(x)

        self.population = new_population

    def mutation(self):
        for i in self.population:
            # r = random.random()
            # if r <= mut:
            i = GeneticOperator.mutation(i, self.mut)

    def crossover(self):
        c = []
        after_crossover = []
        print("Przed krzyżowanie ", self.population)
        for i in self.population:
            r = random.random()
            if r <= self.cros:
                c.append(i)
        print("Doszło 0")
        if len(c) < len(self.population):
            print("Weszło")
            # print("Długość N: ", N_)
            # print("Długość przed: ", len(c))
            for i in range((len(self.population) - len(c))):
                r = random.randint(0, len(c) - 1)
                print(len(c) - 1)
                c.append(c[r])
            # print("Długość po: ", len(c))
        print("Doszło 1")
        unpaired = False
        if len(c) % 2 != 0:  # musi być parzyscie do krzyżowania
            c.append(c[0])
            unpaired = True


        ax = c[:len(c) // 2]
        ay = c[len(c) // 2:]
        print("Doszło 2")
        for i in range(0, len(ax)):
            o1, o2 = GeneticOperator.crossover(ax[i], ay[i])
            after_crossover.append(o1)
            after_crossover.append(o2)
        print("Doszło 3")
        if unpaired:  # Do krzyżowania jest potrzerbna parzysta liczba osobników, ale nie może być ich po krzyżowaniu więcej niż N_ więc usuwamy ostatniego
            # print("Przed: ", after_crossover)
            del after_crossover[-1]
            # print("Po: ", after_crossover)
            unpaired = False
        # print("Krzyżowanie ", after_crossover)

        self.population = after_crossover
        print("Po krzyżowaniu ", self.population)

    def rulette_wheele(self):
        r = RuletteWheele(self.population)
        self.population = r.get_chosen()

    def tournament_selection(self, k):
        # ToDo
        # Zrobić toooooooooooooooooooooooooooo!!!!!!!!!!!!!!!!
        ts = TournamentSelection(self.population, k)
        after_ts = ts.tournament()
        self.population = after_ts

    def toBinary(self):
        bin_population = []
        for i in self.population:
            t = []

            for j in i[:self.n]:
                t.append(Conversion.to_binary(j, self.A, self.B, self.chromosome_length))
            b = Conversion.connect_multi_variable(t)
            t = []
            t.append(b)
            t.append(i[-1])
            bin_population.append(t)
        self.population = bin_population

    def create_fitness(self):
        print("Doszło 2.5")
        print(self.population)
        for i in self.population:
            if self.function == 0:
                fitness = 1 / FunctionsAndFittnes.rosenbrock(i)
            elif self.function == 1:
                fitness = 1 / FunctionsAndFittnes.sphere(i)
            elif self.function == 2:
                fitness = 1 / FunctionsAndFittnes.shekels_foxholes(i, self.n)

            i.append(fitness)

    def create_populations(self):
        population = []
        for i in range(self.popu):
            variables = []
            for j in range(0, self.n):
                r = Conversion.rand_precision_range(self.precision, self.A, self.B)
                variables.append(r)
            population.append(variables)
        return population
