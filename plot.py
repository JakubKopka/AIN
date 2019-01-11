import sys
from PyQt5.QtWidgets import *

from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random

import tkinter as tk
from tkinter import filedialog

import matplotlib.pyplot as plt
import numpy as np
import wave

import ctypes

class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        self.canvas2 = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar2 = NavigationToolbar(self.canvas2, self)

        # Just some button connected to `plot` method
        self.button2 = QPushButton('Załaduj')
        self.button2.clicked.connect(self.plot)
        self.button3 = QPushButton('Załaduj')
        self.button3.clicked.connect(self.plot)
        self.button4 = QPushButton('Nagraj')
        self.button4.clicked.connect(self.record)
        menuBar = QHBoxLayout()


        menuBar.addWidget(self.button2)
        menuBar.addWidget(self.button3)
        menuBar.addWidget(self.button4)


        # set the layout
        layout = QVBoxLayout()

        layout.addLayout(menuBar)

        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)




        self.setLayout(layout)


        self.show()
    def pomPlot(self, filename):
        import matplotlib.pyplot as plt

        import numpy as np
        import wave

        # create file choose dialog and get path to the resource


        plt.subplot(2, 1, 1)

        plt.grid()

        spf = wave.open(filename, 'r')

        # Extract Raw Audio from Wav File
        signal = spf.readframes(-1)
        signal = np.fromstring(signal, 'Int16')
        fs = spf.getframerate()

        Time = np.linspace(0, len(signal) / fs, num=len(signal))

        plt.subplot(2, 1, 2)
        plt.figure(1)
        return plt.plot(Time, signal)
        # plt.show()

    def plot(self):
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename()

        # spf = wave.open(file_path, 'r')
        #
        # signal = spf.readframes(-1)
        # signal = np.fromstring(signal, 'Int16')
        # fs = spf.getframerate()
        #
        # time = np.linspace(0, len(signal) / fs, num=len(signal))
        #
        # plt.figure("Zadanie 1, Jakub Kopka 99202")
        # plt.title(' kanały: {}  rozmiar próbki: {}  \nczęstość próbkowania: {},  ilość próbek: {}'.format(
        #     spf.getnchannels(), spf.getsampwidth(), spf.getframerate(), spf.getnframes()))
        # plt.plot(time, signal)
        # plt.xlabel('czas (s)')
        # plt.ylabel('Amplituda')
        # # plt.show()
        #
        # ''' plot some random stuff '''
        # # random data
        # data = [random.random() for i in range(10)]
        #
        # # instead of ax.hold(False)
        # self.figure.clear()
        #
        # # create an axis
        # ax = self.figure.add_subplot(111)
        #
        # # discards the old graph
        # # ax.hold(False) # deprecated, see above
        #
        # # plot data
        # ax.plot(time, signal)
        #
        # # refresh canvas
        # self.canvas.draw()
        # plt.figure(1)  # the first figure
        # plt.subplot(211)  # the first subplot in the first figure
        # plt.plot([1, 2, 3])
        # plt.subplot(212)  # the second subplot in the first figure
        # plt.plot([4, 5, 6])
        #
        # plt.figure("Zadanie 1, Jakub Kopka 99202")
        # # plt.title(' kanały: {}  rozmiar próbki: {}  \nczęstość próbkowania: {},  ilość próbek: {}'.format(
        # #     spf.getnchannels(), spf.getsampwidth(), spf.getframerate(), spf.getnframes()))
        # plt.plot([1, 2, 3])
        # plt.xlabel('czas (s)')
        # plt.ylabel('Amplituda')
        #
        # plt.figure(2)  # a second figure
        # plt.plot([4, 5, 6])  # creates a subplot(111) by default

        # plt.figure(1)  # figure 1 current; subplot(212) still current
        # plt.subplot(211)  # make subplot(211) in figure1 current
        # plt.title('Easy as 1,2,3')  # subplot 211 title

        self.pomPlot(file_path)

        self.canvas.draw()

    def record(self):
        import pyaudio
        import wave

        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        CHUNK = 1024
        RECORD_SECONDS = 10
        WAVE_OUTPUT_FILENAME = "file.wav"

        audio = pyaudio.PyAudio()

        # start Recording
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)
        print("recording...")
        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print
        "finished recording"

        # stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()

        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()

        self.pomPlot('file.wav')

        self.canvas.draw()

if __name__ == '__main__':
    height = 450;
    width = 600;

    x = width + 200
    y = height+200

    app = QApplication(sys.argv)

    main = Window()
    main.setGeometry(x,y, width, height)
    main.show()


    sys.exit(app.exec_())