import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pykorbit

from_class = uic.loadUiType("Mywindow2.ui")[0]


class MyWindow(QMainWindow, from_class):    # QMainWinodw를 상속 받음
    def __init__(self):
        super().__init__()      # 부모클래스의 함수를 사용하겠다.
        self.setupUi(self)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.inquiry)
        

    def inquiry(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))
        ePrice = pykorbit.get_current_price("ETH")
        self.lineEdit_2.setText(str(ePrice))


app = QApplication(sys.argv)
window = MyWindow()
window.show()   # 윈도우를 열고
app.exec_()     # 윈도우를 연 상태로 대기
