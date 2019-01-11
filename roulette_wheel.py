import random
from random import seed




class RuletteWheele:
    chromosomes = []

    def __init__(self):
        self.chromosomes = [['0010001', 1.245], ["0100000", 1.658], ["0100010", 1.8]]
        self.get_probability_dict()

    def __init__(self, chromosomes):
        self.chromosomes = chromosomes
        self.get_probability()



    def get_probability(self):
        suma = 0
        for i in self.chromosomes:
            suma = suma + i[-1]

        total_fit = float(suma)

        for i in self.chromosomes:
            i[-1] = i[-1] / total_fit



    def roulette_wheel_pop(self):
        chosen = []
        while True:
            for i in self.chromosomes:
                if len(chosen) >= len(self.chromosomes):
                    return chosen
                r = random.random()
                if r <= i[-1]:
                    chosen.append(i[0])

        return chosen

    def get_chosen(self):
        return self.roulette_wheel_pop()


# r = RuletteWheele([['0010001', 1.245], ["0100000", 1.658], ["0100010", 1.8]])
# print(r.get_chosen())