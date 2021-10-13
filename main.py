from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.player = True
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('xo')
        self.buttons_n=[]
        self.game()
        for i in range(3):
            for j in range(3):
                btn = QPushButton(self)
                btn.resize(100, 100)
                btn.move(i*100, j*100)
                btn.clicked.connect(self.game)
                self.buttons_n.append(btn)
        self.show()
    def game(self):
        if self.player:
            for i in self.buttons_n:
                if self.sender()==i:
                    i.setText('x')
                    self.win[self.buttons_n.index(i)]=1
                    self.player = False
        elif not self.player:
            for i in self.buttons_n:
                if self.sender() == i:
                    i.setText('x')
                    self.win[self.buttons_n.index(i)] = 4
                    self.player = True
        winany = [(self.win[0],self.win[1],self.win[2]),
                  (self.win[3], self.win[4], self.win[5]),
                  (self.win[6], self.win[7], self.win[8]),
                  (self.win[0], self.win[3], self.win[6]),
                  (self.win[1], self.win[4], self.win[7]),
                  (self.win[2], self.win[5], self.win[8]),
                  (self.win[0], self.win[4], self.win[8]),
                  (self.win[2], self.win[4], self.win[6])]
        for i in winany:
            if sum(i)==3:
                winner = QMessageBox()
                winner.setWindowTitle('xd')
                winner.setText('winner x')
                winner.exec()
                sys.exit(app.exec_())
            elif sum(i)==12:
                winner = QMessageBox()
                winner.setWindowTitle('xd')
                winner.setText('winner o')
                winner.exec()
                sys.exit(app.exec_())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()

    app.exec()