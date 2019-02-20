import itertools
import random
import textwrap
from pathlib import Path


class Conversion:

    @staticmethod
    def to_binary(d, A, B, chromosome_length):
        b = ((d * (pow(2, chromosome_length)) - (A * (pow(2, chromosome_length))))) / (B - A)
        return bin(int(b)).replace("0b", "").zfill(chromosome_length)

    @staticmethod
    def to_decimal(b, A, B, chromosome_length, precision):
        binary = int(b, 2)
        x = ((B - A) * binary) / (pow(2, chromosome_length) - 1) + A
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

    @staticmethod
    def save_best_and_avg(obj):
        path_absolute = Path().absolute()
        data = "# \tIlosc uruchomien AG: {}\n" \
               "# \tZiarno: {}\n" \
               "# \tRozmiar populacji: {}\n" \
               "# \tLiczba generacji: {}\n" \
               "# \tTyp Selekcji: {}\n" \
               "# \tPrecyzja wyniku: {}\n" \
               "# \tPrawdopodobienstwo krzyzowania: {}\n" \
               "# \tPrawdopodobienstwo mutacji: {}\n" \
               "# \tFunkcja: {}\n" \
               "# \tIlosc zmiennych: {}\n" \
               "# \tPrzedzial: {};{}\n".format(obj.number_iter, obj.seed, obj.popu, obj.generation_number,
                                               obj.selection_type, obj.precision, obj.cros, obj.mut, obj.function,
                                               obj.n, obj.A, obj.B)

        print(data)
        print("Best")
        print(obj.iter_best)
        print("AVG")
        print(obj.iter_avg)
        with open('best.txt', 'w') as file:
            file.write(data)
            file.write("#Skrypt do Gnuplota:\n")
            l = "#set style data lines\n#plot '{}\\best.txt'".format(path_absolute)
            for i in range(0, len(obj.iter_avg)):
                if i == 0:
                    l = l + " using 1:{}, ".format(i + 2)
                else:
                    l = l + "'' using 1:{}, ".format(i + 2)
            l = l[:len(l) - 2]
            l = l + "\n"
            file.write(l)
            file.write("#numer_iteracji \t #iter_1 \t #iter_2 \n")
            # line = ""
            for i in range(0, len(obj.iter_best[0])):
                line = "{} \t".format(i + 1)
                for j in range(0, len(obj.iter_best)):
                    line = line + "{} \t".format(obj.iter_best[j][i])
                line = line + "\n"
                file.write(line)
        with open('avg.txt', 'w') as file:
            file.write(data)
            file.write("#Skrypt do Gnuplota:\n")
            l = "#set style data lines\n#plot '{}\\avg.txt'".format(path_absolute)
            for i in range(0, len(obj.iter_avg)):
                if i == 0:
                    l = l + " using 1:{}, ".format(i + 2)
                else:
                    l = l + "'' using 1:{}, ".format(i + 2)
            l = l[:len(l) - 2]
            l = l + "\n"
            file.write(l)
            file.write("#numer_iteracji \t #iter_1 \t #iter_2 \n")
            for i in range(0, len(obj.iter_avg[0])):
                line = "{} \t".format(i + 1)
                for j in range(0, len(obj.iter_avg)):
                    line = line + "{} \t".format(obj.iter_avg[j][i])
                line = line + "\n"
                file.write(line)
