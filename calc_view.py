# -*- coding: utf-8 -*-
""" calc_view.py - presenter for the default calculator"""
__author__ = "topseli"
__license__ = "0BSD"


import os
import sys
import logging

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox

# Import for eval function
from math import sqrt, sin, cos, tan # noqa F401


class CalcView(QtWidgets.QWidget):

    def __init__(self):
        super(CalcView, self).__init__()
        self.init_ui()

    def init_ui(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '/calc_view.ui'
        uic.loadUi(path, self)

    def show_warning(self, e):
        self.input_calculation.setText("Error")
        logging.info(e)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Warning")
        msg.setText("An error occured!")
        msg.setDetailedText(str(e))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    @pyqtSlot()
    def on_button_0_clicked(self):
        self.input_calculation.insert("0")

    @pyqtSlot()
    def on_button_1_clicked(self):
        self.input_calculation.insert("1")

    @pyqtSlot()
    def on_button_2_clicked(self):
        self.input_calculation.insert("2")

    @pyqtSlot()
    def on_button_3_clicked(self):
        self.input_calculation.insert("3")

    @pyqtSlot()
    def on_button_4_clicked(self):
        self.input_calculation.insert("4")

    @pyqtSlot()
    def on_button_5_clicked(self):
        self.input_calculation.insert("5")

    @pyqtSlot()
    def on_button_6_clicked(self):
        self.input_calculation.insert("6")

    @pyqtSlot()
    def on_button_7_clicked(self):
        self.input_calculation.insert("7")

    @pyqtSlot()
    def on_button_8_clicked(self):
        self.input_calculation.insert("8")

    @pyqtSlot()
    def on_button_9_clicked(self):
        self.input_calculation.insert("9")

    @pyqtSlot()
    def on_button_dot_clicked(self):
        self.input_calculation.insert(".")

    @pyqtSlot()
    def on_button_plus_clicked(self):
        self.input_calculation.insert("+")

    @pyqtSlot()
    def on_button_minus_clicked(self):
        self.input_calculation.insert("-")

    @pyqtSlot()
    def on_button_multiply_clicked(self):
        self.input_calculation.insert("*")

    @pyqtSlot()
    def on_button_divide_clicked(self):
        self.input_calculation.insert("/")

    @pyqtSlot()
    def on_button_modulo_clicked(self):
        self.input_calculation.insert("%")

    @pyqtSlot()
    def on_button_sin_clicked(self):
        self.input_calculation.insert("sin()")

    @pyqtSlot()
    def on_button_cos_clicked(self):
        self.input_calculation.insert("cos()")

    @pyqtSlot()
    def on_button_tan_clicked(self):
        self.input_calculation.insert("tan()")

    @pyqtSlot()
    def on_button_sqrt_clicked(self):
        self.input_calculation.insert("sqrt()")

    @pyqtSlot()
    def on_button_clear_clicked(self):
        self.input_calculation.clear()

    @pyqtSlot()
    def on_button_equals_clicked(self):
        calculation = self.input_calculation.text()
        if calculation.count("Error") or calculation.count("=") != 0 or len(calculation) < 1:
            self.input_calculation.clear()
            logging.info("No calculation")
        else:
            try:
                result = calculation + "=" + str(eval(calculation))
                self.input_calculation.setText(result)
                logging.info(result)
            except Exception as e:
                self.show_warning(e)


def run():
    APP = QtWidgets.QApplication(sys.argv)
    APP_WINDOW = CalcView()
    APP_WINDOW.button_exit.clicked.connect(sys.exit)
    APP_WINDOW.show()
    APP.exec_()


if __name__ == '__main__':

    @pyqtSlot()
    def on_button_equals_clicked(self):
        calculation = self.input_calculation.text()

        if calculation.count("=") != 0 or len(calculation) < 1:
            self.input_calculation.clear()
        else:
            self.input_calculation.setText(calculation + "=" + str(eval(calculation)))

    run()
