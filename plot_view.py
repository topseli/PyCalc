# -*- coding: utf-8 -*-
""" calc_view.py - presenter for the default calculator"""
__author__ = "topseli"
__license__ = "0BSD"


import os
import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure


class PlotCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)

        self.axes = fig.add_subplot(111)
        super(PlotCanvas, self).__init__(fig)


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
        self.grid_layout.addWidget(toolbar, 3, 0, 1, 3)
        self.grid_layout.addWidget(self.canvas, 4, 0, 1, 3)

    def show_warning(self, e):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        # TODO define better error message
        msg.setText("Some error")
        msg.setWindowTitle("ERROR")
        msg.setDetailedText(str(e))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    @pyqtSlot()
    def on_plot_button_clicked(self):
        # equation = self.equation_input.text()
        # self.x = numpy.array(range(100))
        self.canvas.axes.plot([1, 2, 3, 4, 5], [3, 1, 4, 2, 5])
        self.canvas.draw()


def run():
    APP = QtWidgets.QApplication(sys.argv)
    APP_WINDOW = PlotView()
    APP_WINDOW.exit_button.clicked.connect(sys.exit)
    APP_WINDOW.show()
    APP.exec_()


if __name__ == '__main__':
    run()
