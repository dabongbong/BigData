import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit

from_class =uic.loadUiType("Mywindow.ui")[0]

class MyWindow(QMainWindow,from_class):    # QMainWinodw를 상속 받음
    def __init__(self):
        super().__init__()      # 부모클래스의 함수를 사용하겠다.
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry)

    def inquiry(self):
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))
        ePrice = pykorbit.get_current_price("ETH")
        self.lineEdit_2.setText(str(ePrice))



app = QApplication(sys.argv)
window = MyWindow()
window.show()   # 윈도우를 열고
app.exec_()     # 윈도우를 연 상태로 대기
