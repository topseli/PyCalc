# -*- coding: utf-8 -*-
""" calc_view.py - presenter for the default calculator"""
__author__ = "topseli"
__license__ = "0BSD"


import os
import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
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
        equation = self.equation_input.text()
        print(equation)


def run():
    APP = QtWidgets.QApplication(sys.argv)
    APP_WINDOW = PlotView()
    APP_WINDOW.exit_button.clicked.connect(sys.exit)
    APP_WINDOW.show()
    APP.exec_()


if __name__ == '__main__':
    run()
