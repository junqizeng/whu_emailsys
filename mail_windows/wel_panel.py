from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt


class WelPanel:
    def __init__(self, main_window):
        self.wel_slogan = QLabel(main_window)
        self.wel_slogan.resize(500, 35)
        self.wel_slogan.setStyleSheet('font-size:16px;font-weight:bold;font-family:SimHei;')
        self.wel_slogan.move(10, 10)

        self.account_slogan = QLabel(main_window)
        self.account_slogan.resize(620, 300)
        self.account_slogan.setAlignment(Qt.AlignCenter)
        self.account_slogan.setStyleSheet('font-size:18px;font-weight:bold;font-family:SimHei;')
        self.account_slogan.move(200, 55)

    def update(self, mail_acc, mail_stats):
        self.wel_slogan.setText(f'   欢迎你，{mail_acc}!')
        mail_num = mail_stats.split(' ')[1]
        mail_bytes = mail_stats.split(' ')[2][:-2]
        self.account_slogan.setText(
            f'收信箱统计数据: \n当前收件箱中有{mail_num}封邮件，\n共计大小{mail_bytes}字节')

    def hide(self):
        self.wel_slogan.hide()
        self.account_slogan.hide()

    def show(self):
        self.wel_slogan.show()
        self.account_slogan.show()
