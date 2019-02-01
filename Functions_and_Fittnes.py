class FunctionsAndFittnes():

    @staticmethod
    def sphere(x):
        suma = 0
        for i in x:
            suma = suma + pow(i, 2)
        return suma

    @staticmethod
    def fitness_sphere(x):
        suma = 0
        for i in x:
            suma = suma + pow(i, 2)
        if suma == 0:
            return 0
        else:
            return 1 / suma

    @staticmethod
    def rosenbrock(x):
        suma = 0
        for i in range(0, len(x) - 1):
            suma = suma + 100.0 * (x[i + 1] - x[i] ** 2.0) ** 2.0 + (1 - x[i]) ** 2.0
        return suma

    @staticmethod
    def fitness_rosenbrock(x):
        suma = 0
        for i in range(0, len(x) - 1):
            suma = suma + 100.0 * (x[i + 1] - x[i] ** 2.0) ** 2.0 + (1 - x[i]) ** 2.0
        if suma == 0:
            return 0
        else:
            return 1 / suma

    @staticmethod
    def shekels_foxholes(x, x_numbers):
        a = [
            [-32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32],
            [-32, -32, -32, -32, -32, -16, -16, -16, -16, -16, 0, 0, 0, 0, 0, 16, 16, 16, 16, 16, 32, 32, 32, 32, 32]
        ]
        # https://al-roomi.org/benchmarks/unconstrained/2-dimensions/7-shekel-s-foxholes-function

        suma_j = 1/500
        for j in range(0, pow(5, x_numbers)):
            suma_i = j;
            for i in range(0, x_numbers):
                suma_i = suma_i + pow((x[i] - a[i][j]), 6)
            suma_j = suma_j + 1/suma_i

        return 1/suma_j



    def fitness_foxholes(x):
        pass


# print(FunctionsAndFittnes.shekels_foxholes([0,-38], 2))