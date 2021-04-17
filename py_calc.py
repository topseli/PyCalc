# -*- coding: utf-8 -*-
""" py_calc.py - Main class for a simple GUI calculator"""
__author__ = "topseli"
__license__ = "0BSD"

import sys
import os
import logging
from PyQt5 import QtWidgets, uic
import calc_view
import plot_view
version = "0.2"


class PyCalc(QtWidgets.QWidget):

    def __init__(self):
        super(PyCalc, self).__init__()
        self.init_ui()
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info("PyCalc version %s started" % version)

    def init_ui(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '/main_window.ui'
        uic.loadUi(path, self)

        # Create QWidget instances
        self.calc_widget = calc_view.CalcView()
        self.plot_widget = plot_view.PlotView()

        # Add QWidget instances to tabWidget
        self.tab_widget.addTab(self.calc_widget, "Calculate")
        self.tab_widget.addTab(self.plot_widget, "Plot")

        # Connect exit_buttons
        self.calc_widget.exit_button.clicked.connect(
            self.on_exit_button_clicked)
        self.plot_widget.exit_button.clicked.connect(
            self.on_exit_button_clicked)

    def on_exit_button_clicked(self):
        logging.info("Exiting")
        sys.exit(0)


def run():
    APP = QtWidgets.QApplication(sys.argv)
    APP_WINDOW = PyCalc()
    APP_WINDOW.show()
    APP.exec_()


if __name__ == '__main__':
    run()
