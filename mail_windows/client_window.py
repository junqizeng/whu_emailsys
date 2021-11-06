from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon


class ClientWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(850, 650)
        self.setWindowTitle('武汉大学邮箱系统')
        self.move(int((QApplication.desktop().width()-self.width())*0.5),
                  int((QApplication.desktop().height()-self.height())*0.5))
        self.setWindowIcon(QIcon('D:/project/email/mail_windows/image/whu.png'))

        self.write_btn = QPushButton(self)
        self.write_btn.resize(180, 50)
        self.write_btn.move(15, 55)
        self.write_btn.setStyleSheet('background-color:white;font-size:16px;')
        self.write_btn.setText('写 信')

        self.receiver_btn = QPushButton(self)
        self.receiver_btn.resize(180, 50)
        self.receiver_btn.move(15, 115)
        self.receiver_btn.setStyleSheet('background-color:white;font-size:16px')
        self.receiver_btn.setText('收 信')
