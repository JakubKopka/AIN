import random
from random import seed


class TournamentSelection():
    chromosomes = []
    k_size = 0

    def __init__(self, chromosomes, k_size):
        self.chromosomes = chromosomes
        self.k_size = k_size

    def tournament(self):

        if self.k_size:
            new_population = []

            while len(new_population) <= len(self.chromosomes):
                tour = []
                for i in range(0, (self.k_size * self.k_size)):
                    r = random.randint(0, len(self.chromosomes) - 1)
                    for iter, i in enumerate(self.chromosomes):
                        if r == iter:
                            tour.append(i[-1])
                # print(tour)
                max_ = max(tour)
                for i in self.chromosomes:
                    if i[-1] is max_:
                        new_population.append(i[0])
            return new_population


# ts = TournamentSelection([['111100000', 1.2], ['10001', 1.3], ['10101', 1.4]], 2)
# print(ts.tournament())
