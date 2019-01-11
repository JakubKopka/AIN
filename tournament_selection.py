import random
from random import seed



class TournamentSelection():
    chromosomes_fitness = {}
    k_size = 0

    def __init__(self, chromosomes_fitness, k_size):
        self.chromosomes_fitness = chromosomes_fitness
        self.k_size = k_size

    def tournament(self):

        if self.k_size:
            new_population = []

            while len(new_population) <= len(self.chromosomes_fitness):
                tour = {}
                for i in range(0, self.k_size):
                    r = random.randint(0, len(self.chromosomes_fitness) - 1)
                    for (iter, dict_) in enumerate(self.chromosomes_fitness):
                        if r == iter:
                            tour[dict_] = self.chromosomes_fitness[dict_]
                max_ = max(tour, key=tour.get)
                new_population.append(max_)
        print(new_population)


ts = TournamentSelection({'1111': 1.2, '10001': 1.3, '10101': 1.4}, 2)
ts.tournament()
