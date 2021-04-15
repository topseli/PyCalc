# -*- coding: utf-8 -*-
""" calc_view.py - presenter for the default calculator"""
__author__ = "topseli"
__license__ = "0BSD"


import os
import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QMessageBox


class CalcView(QtWidgets.QWidget):

    equals_signal = pyqtSignal(str)

    def __init__(self):
        super(CalcView, self).__init__()
        self.init_ui()

    def init_ui(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '/calc_view.ui'
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
    def on_button_0_clicked(self):
        self.calculation_input.setText(self.calculation_input.text() + "0")

    @pyqtSlot()
    def on_button_1_clicked(self):
        self.calculation_input.setText(self.calculation_input.text() + "1")

    @pyqtSlot()
    def on_button_2_clicked(self):
        self.calculation_input.setText(self.calculation_input.text() + "2")

    @pyqtSlot()
    def on_button_3_clicked(self):
        self.calculation_input.setText(self.calculation_input.text() + "3")

    @pyqtSlot()
    def on_button_4_clicked(self):
        self.calculation_input.setText(self.calculation_input.text() + "4")

    @pyqtSlot()
    def on_button_5_clicked(self):
        self.calculation_input.setText(self.calculation_input.text() + "5")

    @pyqtSlot()
    def on_button_6_clicked(self):
        self.calculation_input.setText(self.calculation_input.text() + "6")

    @pyqtSlot()
    def on_button_7_clicked(self):
        self.calculation_input.setText(self.calculation_input.text() + "7")

    @pyqtSlot()
    def on_button_8_clicked(self):
        self.calculation_input.setText(self.calculation_input.text() + "8")

    @pyqtSlot()
    def on_button_9_clicked(self):
        self.calculation_input.setText(self.calculation_input.text() + "9")

    @pyqtSlot()
    def on_button_dot_clicked(self):
        self.calculation_input.setText(self.calculation_input.text() + ".")

    @pyqtSlot()
    def on_button_plus_clicked(self):
        self.calculation_input.setText(self.calculation_input.text() + "+")

    @pyqtSlot()
    def on_button_minus_clicked(self):
        self.calculation_input.setText(self.calculation_input.text() + "-")

    @pyqtSlot()
    def on_equals_button_clicked(self):
        calculation = self.calculation_input.text()
        self.equals_signal.emit(calculation)


def run():
    APP = QtWidgets.QApplication(sys.argv)
    APP_WINDOW = CalcView()
    APP_WINDOW.exit_button.clicked.connect(sys.exit)
    APP_WINDOW.show()
    APP.exec_()


if __name__ == '__main__':

    @pyqtSlot()
    def on_equals_button_clicked(self):
        calculation = self.calculation_input.text()

        if calculation.count("=") != 0 or len(calculation) < 1:
            calculation = ""
            self.calculation_input.setText(calculation)
        else:
            self.calculation_input.setText(calculation + "=" + str(eval(calculation)))

    run()
