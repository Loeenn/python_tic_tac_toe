from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import sys
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100,400, 600)
        self.game()
        self.show()
        self.setWindowTitle("Крестики-нолики")
    def game(self):
        self.turn = random.randint(0, 1)
        self.times = 0
        self.butt = []
        for _ in range(3):
            temp = []
            for _ in range(3):
                temp.append((QPushButton(self)))
            self.butt.append(temp)
        x = y = 100
        for i in range(3):
            for j in range(3):
                self.butt[i][j].setGeometry(x * i + 60,y * j + 180, 80, 80)
                self.butt[i][j].clicked.connect(self.winner)
        self.tablo = QLabel(self)
        self.tablo.setGeometry(70,100, 260, 60)
        self.tablo.setAlignment(Qt.AlignCenter)
    def winner(self):
        self.times += 1
        button = self.sender()
        button.setEnabled(False)
        if self.turn == 1:
            button.setText("O")
            self.turn = 0
        else:
            button.setText("X")
            self.turn = 1
        win = self.games()
        whowin = ""
        if win == True:
            if self.turn == 1:
                whowin = "Победил X"
            else:
                whowin = "Победил O"
            for buttons in self.butt:
                for push in buttons:
                    push.setEnabled(False)
        elif self.times == 9:
            whowin = "Ничья"
        self.tablo.setText(whowin)
    def games(self):
        for i in range(3):
            if self.butt[0][i].text() == self.butt[1][i].text()  and self.butt[0][i].text() == self.butt[2][i].text()  and self.butt[0][i].text() != "":
                return True
        for i in range(3):
            if self.butt[i][0].text() == self.butt[i][1].text()  and self.butt[i][0].text() == self.butt[i][2].text()  and self.butt[i][0].text() != "":
                return True
        if self.butt[0][0].text() == self.butt[1][1].text()and self.butt[0][0].text() == self.butt[2][2].text() and self.butt[0][0].text() != "":
            return True
        if self.butt[1][1].text() == self.butt[2][0].text() and self.butt[0][2].text() == self.butt[1][1].text()and self.butt[0][2].text() != "":
            return True
        return False
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())