# importing required libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class Ui_Widget(QtWidgets.QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.player = "X"
        self.fieldLayouts = []
        self.fields = []
        self.layout = QVBoxLayout()

        # Create nine buttons
        for x in range(9):
            self.fields.append(QPushButton(""))

        # Connect the buttons
        for x in self.fields:
            self.connect(x, QtCore.SIGNAL('clicked()'), self.fieldClicked)
            self.x.clicked.connect(self.fieldClicked)


        # Create three QHBoxLayouts for buttons
        for x in range(3):
            self.fieldLayouts.append(QHBoxLayout())

        # Fill the layouts (3x3)
        i = 0
        for x in self.fieldLayouts:
            for y in range(3):
                x.addWidget(self.fields[i])
                i = i + 1

        # Add the layouts to the main layout
        for x in self.fieldLayouts:
            self.layout.addLayout(x)

        # Set the main layout
        self.setLayout(self.layout)

    def fieldClicked(self):
        button = self.sender()

        if str(button.text()) == "":
            button.setText(self.player)
            self.check()
            self.changePlayer()

    def changePlayer(self):
        self.player = 'X' if self.player == 'O' else 'O'

    def check(self):
        val = []
        for x in self.fields:
            val.append(x.text())

        # horizontal check
        if val[0] == val[1] == val[2] != "": self.win()
        if val[3] == val[4] == val[5] != "": self.win()
        if val[6] == val[7] == val[8] != "": self.win()

        # vertical check
        if val[0] == val[3] == val[6] != "": self.win()
        if val[1] == val[4] == val[7] != "": self.win()
        if val[2] == val[5] == val[8] != "": self.win()

        # diagonal check
        if val[0] == val[4] == val[8] != "": self.win()
        if val[6] == val[4] == val[2] != "": self.win()

    def win(self):
        QMessageBox.information(self, "Winner!", "Player " + self.player + " has won")

        # Reset fields
        for x in self.fields:
            x.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a =Ui_Widget()
    a.show()

    sys.exit(app.exec_())