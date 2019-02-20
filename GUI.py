import random
import sys
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import ctypes

import wave

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from matplotlib import pylab
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from Functions_and_Fittnes import FunctionsAndFittnes
from Genetic_Algorithm import GeneticAlgorithm


from matplotlib import cm
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plot


class FunctionWindow(QDialog):
    def __init__(self, parent=None):
        super(FunctionWindow, self).__init__(parent)


class Window(QDialog):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.start = QPushButton('Start')
        self.start.clicked.connect(self.startAG)

        self.show_function = QPushButton('Podgląd funkcji')
        self.show_function.clicked.connect(self.show_f)

        self.iter_text = QLabel("Ilość uruchomień AG:")
        self.iter = QLineEdit()
        self.iter.setText("1")

        self.ag = QLabel("Ustawienia AG")
        self.f_ = QLabel("Ustawienia funkcji")
        self.text_N = QLabel("Rozmiar populacji")
        self.text_n = QLabel("Ilość zmiennych")
        self.text_generation_number = QLabel("Liczba generacji")
        self.text_selection = QLabel("Typ selekcji")
        self.text_precision = QLabel("Precyzja wyniku")
        self.text_cros = QLabel("Prawdopodobieństow krzyżowania")
        self.text_mut = QLabel("Prawdopodobieństow mutacji")
        self.text_function = QLabel("Funkcja")
        self.text_interval = QLabel("Przedział")
        self.text_seed = QLabel("Ziarno")
        self.informacje = QLabel("")
        self.ag.setStyleSheet("font: 13pt")
        self.ag.setAlignment(Qt.AlignCenter)
        self.f_.setStyleSheet("font: 13pt")
        self.f_.setAlignment(Qt.AlignCenter)

        # Ustawienie funkci
        self.function = QComboBox()
        self.function.addItem("Rosenbrock")
        self.function.addItem("Sphere")
        self.function.addItem("Shekel's Foxholes")

        # Typ selekcji
        self.selection_type = QComboBox()
        self.selection_type.addItem("Koło ruletki")
        self.selection_type.addItem("Seleckja Turniejowa k=2")
        self.selection_type.addItem("Seleckja Turniejowa k=3")
        self.selection_type.addItem("Seleckja Turniejowa k=4")
        self.selection_type.addItem("Seleckja Turniejowa k=5")

        # Prawdopoodbieństwo i mutacja
        self.cros = QLineEdit()
        self.cros.setText("0.9")
        self.mut = QLineEdit()
        self.mut.setText("0.01")

        # Dokładność wyniku
        self.precision = QComboBox()
        self.precision.addItem("10 do -2")
        self.precision.addItem("10 do -3")
        self.precision.addItem("10 do -4")
        self.precision.addItem("10 do -5")
        self.precision.addItem("10 do -6")

        # Liczba generacji
        self.generation_number = QLineEdit()
        self.generation_number.setText("100")

        # Rozmiar populacji
        self.population = QLineEdit()
        self.population.setText("500")

        # Ilosć zmiennych
        self.n = QLineEdit()
        self.n.setText("2")

        # Przedział funkcji
        self.interval = QLineEdit()
        self.interval.setText("-2.5;3")

        # Ziarno
        self.seed = QLineEdit()

        menu = QVBoxLayout()
        splitter1 = QSplitter(Qt.Vertical)
        menu.addWidget(splitter1)
        menu.addWidget(splitter1)
        splitter1.addWidget(self.ag)
        splitter1.setSizes([1, 2])

        menu.addWidget(self.iter_text)
        menu.addWidget(self.iter)
        menu.addWidget(self.text_seed)
        menu.addWidget(self.seed)

        menu.addWidget(self.ag)

        menu.addWidget(self.text_N)
        menu.addWidget(self.population)

        menu.addWidget(self.text_generation_number)
        menu.addWidget(self.generation_number)

        menu.addWidget(self.text_selection)
        menu.addWidget(self.selection_type)

        menu.addWidget(self.text_precision)
        menu.addWidget(self.precision)

        menu.addWidget(self.text_cros)
        menu.addWidget(self.cros)

        menu.addWidget(self.text_mut)
        menu.addWidget(self.mut)


        menu.addWidget(splitter1)

        menu.addWidget(self.f_)
        menu.addWidget(self.text_function)
        menu.addWidget(self.function)
        menu.addWidget(self.show_function)
        menu.addWidget(self.text_n)
        menu.addWidget(self.n)
        menu.addWidget(self.text_interval)
        menu.addWidget(self.interval)

        # menu.addWidget(self.sl)
        menu.addWidget(self.start)

        splitter1 = QSplitter(Qt.Vertical)
        menu.addWidget(splitter1)
        menu.addWidget(splitter1)
        splitter1.addWidget(self.ag)

        splitter1.setSizes([1, 2])

        wykres = QVBoxLayout()

        wykres.addWidget(self.toolbar)
        wykres.addWidget(self.canvas)

        layout = QHBoxLayout()
        layout.addLayout(wykres, 80)
        layout.addLayout(menu, 20)

        self.setLayout(layout)
        self.show()

    def show_f(self):
        class NewDialog(QDialog):
            def __init__(self, parent):
                super(NewDialog, self).__init__(parent)

        self.nd = NewDialog(self)

        fig = plot.figure()
        ax = fig.gca(projection='3d')
        X = None
        Y = None
        Z = None
        if self.function.currentIndex() == 1:
            s = 1
            X = np.arange(-10, 10. + s, s)
            Y = np.arange(-10, 10. + s, s)
            X, Y = np.meshgrid(X, Y)
            Z = FunctionsAndFittnes.sphere([X, Y])

        elif self.function.currentIndex() == 0:
            s = 0.1
            X = np.arange(-2, 2. + s, s)
            Y = np.arange(-1, 3. + s, s)
            X, Y = np.meshgrid(X, Y)
            Z = FunctionsAndFittnes.rosenbrock([X, Y])
        elif self.function.currentIndex() == 2:
            s = 10
            X = np.arange(-80, 80. + s, s)
            Y = np.arange(-80, 80. + s, s)
            X, Y = np.meshgrid(X, Y)
            Z = FunctionsAndFittnes.shekels_foxholes([X, Y], 2)

        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, norm=LogNorm(), cmap=cm.jet)

        canvas = FigureCanvas(fig)
        toolbar = NavigationToolbar(canvas, self)
        fig.canvas.draw()
        wykres = QVBoxLayout()

        wykres.addWidget(toolbar)
        wykres.addWidget(canvas, 1)

        layout = QHBoxLayout()
        layout.addLayout(wykres)
        self.nd.setLayout(layout)
        self.nd.show()


    def startAG(self):
        print("Population:", self.population.text())
        print("Generation Number: ", self.generation_number.text())
        print("Selection: ", self.selection_type.currentIndex(), " ", self.selection_type.currentText())
        print("Precision: ", self.precision.currentIndex() + 2)
        print("Crossover: ", self.cros.text())
        print("Mutation: ", self.mut.text())
        print("Function: ", self.function.currentIndex())
        print("n: ", self.n.text())
        print("Interval: ", self.interval.text())
        print("Seed: ", self.seed.text())
        print("Doszło #0")
        # print(int(self.population.text()), int(self.generation_number.text()),
        #                       self.selection_type.currentIndex(),
        #                       self.precision.currentIndex() + 2, float(self.cros.text()),
        #                       float(self.mut.text()),int(self.function.currentIndex()), int(self.n.text()),
        #       self.interval.text(),  int(self.seed.text())
        #                       )

        if self.seed.text() == "":
            self.seed = "-1"
        else:
            self.seed = int(self.seed.text())

        ga = GeneticAlgorithm(int(self.iter.text()), int(self.population.text()), int(self.generation_number.text()),
                              self.selection_type.currentIndex(),
                              self.precision.currentIndex() + 2, float(self.cros.text()),
                              float(self.mut.text()),
                              int(self.function.currentIndex()), int(self.n.text()), self.interval.text(),
                              self.seed)
        self.plot(list(range(1, len(ga.avg_) + 1)), ga.avg_, list(range(1, len(ga.best_) + 1)), ga.best_)


    def plot(self, x1, y1, x2, y2):
        plt.clf()
        root = tk.Tk()
        root.withdraw()

        plt.subplot(2, 1, 1)
        plt.plot(x1, y1, "r")
        plt.plot(x2, y2, "c")
        plt.xlabel('Numer generacji')
        plt.ylabel('Średnia osobników / Najlepszy osobnik')
        plt.subplot(2, 1, 2)
        plt.plot(x2, y2, "c")
        plt.xlabel('Numer generacji')
        plt.ylabel('Najlepszy osobnik')

        self.canvas.draw()
