# import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QComboBox, QLabel
from PyQt5.QtGui import QIcon


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(535, 375)
        self.setWindowIcon(QIcon('D:/project/email/mail_windows/image/whu.png'))
        self.setWindowTitle('邮箱系统登录')
        self.move(int(QApplication.desktop().width() * 0.357), int(QApplication.desktop().height() * 0.31))

        self.account_le = QLineEdit(self)
        self.account_le.resize(300, 35)
        self.account_le.setStyleSheet('font-size:16px')
        self.account_le.setPlaceholderText("请输入邮箱账号")
        self.account_le.move(int((self.width() - self.account_le.width()) * 0.5), int(self.height() * 0.43))
        self.account_le.resize(180, 35)
        self.account_le.setClearButtonEnabled(True)

        self.account_slogan = QLabel(self)
        self.account_slogan.resize(65, 35)
        self.account_slogan.setText('用户名:')
        self.account_slogan.setStyleSheet('font-size:14px;font-weight:bold;font-family:SimHei')
        self.account_slogan.move(self.account_le.x(), self.account_le.y() - self.account_slogan.height() + 5)

        self.pwd_le = QLineEdit(self)
        self.pwd_le.resize(300, 35)
        self.pwd_le.setStyleSheet('font-size:16px')
        self.pwd_le.move(int((self.width() - self.pwd_le.width()) * 0.5), int(self.height() * 0.60))
        self.pwd_le.setPlaceholderText("请输入邮箱授权码")
        self.pwd_le.setEchoMode(QLineEdit.Password)
        self.pwd_le.setClearButtonEnabled(True)

        self.pwd_slogan = QLabel(self)
        self.pwd_slogan.resize(65, 35)
        self.pwd_slogan.setText('授权码:')
        self.pwd_slogan.setStyleSheet('font-size:14px;font-weight:bold;font-family:SimHei')
        self.pwd_slogan.move(self.pwd_le.x(), self.pwd_le.y() - self.pwd_slogan.height() + 5)

        self.login_btn = QPushButton(self)
        self.login_btn.resize(300, 40)
        self.login_btn.setStyleSheet('font-size:16px')
        self.login_btn.move(int((self.width() - self.login_btn.width()) * 0.5), int(self.height() * 0.75))
        self.login_btn.setText('安全登录')

        self.mails = ['@163.com', '@whu.edu.cn']
        self.mail_choice = QComboBox(self)
        self.mail_choice.addItems(self.mails)
        self.mail_choice.resize(115, 33)
        self.mail_choice.setStyleSheet('font_size:16px')
        self.mail_choice.move(self.account_le.x() + self.account_le.width() + 5, self.account_le.y() + 1)

        self.wel_slogan = QLabel(self)
        self.wel_slogan.resize(250, 33)
        self.wel_slogan.setText('欢迎使用武汉大学邮箱系统')
        self.wel_slogan.setStyleSheet('font-size:19px;font-weight:bold;font-family:SimHei')
        self.wel_slogan.move(int((self.width() - self.wel_slogan.width()) * 0.5), int(self.height() * 0.20))

        self.author_mes = QLabel(self)
        self.author_mes.resize(413, 33)
        self.author_mes.setText('制作者姓名：曾俊淇  学号：2019300003058  仅供学习交流！')
        self.author_mes.setStyleSheet('font-size:14px;font-weight:bold;font-family:SimHei')
        self.author_mes.move(int((self.width() - self.author_mes.width()) * 0.5), int(self.height() * 0.90))


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     login_win = LoginWindow()
#
#     login_win.show()
#
#     sys.exit(app.exec_())
