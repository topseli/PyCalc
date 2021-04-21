# -*- coding: utf-8 -*-
""" plot_view.py - presenter for the graph plotter"""
__author__ = "topseli"
__license__ = "0BSD"


import os
import sys
import logging

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox

# Import for eval function
from numpy import linspace, sqrt, sin, cos, tan # noqa F401

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure


class PlotCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(PlotCanvas, self).__init__(fig)

    def clear(self):
        self.axes.clear()
        self.draw()

    def plot(self, equation):
        # NOTE You can modify the linspace to change the plotting range and precision.
        x = linspace(-5, 5, 100)
        y = eval(equation)
        self.axes.plot(x, y)
        self.draw()


class PlotView(QtWidgets.QWidget):

    def __init__(self):
        super(PlotView, self).__init__()
        self.init_ui()

    def init_ui(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '/plot_view.ui'
        uic.loadUi(path, self)
        # The width and height are arbitrary but fills the window on a 1440p screen
        self.canvas = PlotCanvas(self, width=20, height=16, dpi=100)
        toolbar = NavigationToolbar2QT(self.canvas, self)
        self.grid_layout = self.layout()
        self.grid_layout.addWidget(toolbar, 3, 0, 1, 5)
        self.grid_layout.addWidget(self.canvas, 4, 0, 1, 5)

    def show_warning(self, e):
        self.input_equation.setText("Error")
        logging.info(e)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Warning")
        msg.setText("An error occured!")
        msg.setDetailedText(str(e))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    @pyqtSlot()
    def on_button_clear_clicked(self):
        self.canvas.clear()
        self.input_equation.clear()

    @pyqtSlot()
    def on_button_plot_clicked(self):
        equation = self.input_equation.text()
        try:
            self.canvas.plot(equation)
        except Exception as e:
            self.show_warning(e)


def run():
    APP = QtWidgets.QApplication(sys.argv)
    APP_WINDOW = PlotView()
    APP_WINDOW.button_exit.clicked.connect(sys.exit)
    APP_WINDOW.show()
    APP.exec_()


if __name__ == '__main__':
    run()
