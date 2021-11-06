from PyQt5.QtWidgets import QLineEdit, QLabel, QTextEdit, QPushButton


class WritePanel:
    def __init__(self, main_window):
        self.pos_x = 214
        self.width = 620

        self.state_slogan = QLabel(main_window)
        self.state_slogan.resize(500, 35)
        self.state_slogan.setText(f'   状态: 编辑邮件中······')
        self.state_slogan.setStyleSheet('font-size:16px;font-weight:bold;font-family:SimHei;')
        self.state_slogan.move(10, 10)

        self.sender_lb = QLabel(main_window)
        self.sender_lb.resize(600, 25)
        self.sender_lb.setStyleSheet('font-size:16px;font-weight:bold;font-family:SimHei')
        self.sender_lb.move(self.pos_x, 50)

        self.receiver_lb = QLabel(main_window)
        self.receiver_lb.resize(65, 25)
        self.receiver_lb.setText('收件人:')
        self.receiver_lb.setStyleSheet('font-size:16px;font-weight:bold;font-family:SimHei')
        self.receiver_lb.move(self.pos_x, self.sender_lb.y()+self.sender_lb.height())

        self.receiver_le = QLineEdit(main_window)
        self.receiver_le.resize(self.width, 25)
        self.receiver_le.setStyleSheet('font-size:16px')
        self.receiver_le.setPlaceholderText(" 请输入收件人，不同收件人请用分号隔开")
        self.receiver_le.move(self.pos_x, self.receiver_lb.y() + self.receiver_lb.height())

        self.subject = QLabel(main_window)
        self.subject.resize(65, 25)
        self.subject.setText('主题:')
        self.subject.setStyleSheet('font-size:16px;font-weight:bold;font-family:SimHei')
        self.subject.move(self.pos_x, self.receiver_le.y()+self.receiver_le.height())

        self.subject_le = QLineEdit(main_window)
        self.subject_le.resize(self.width, 25)
        self.subject_le.setStyleSheet('font-size:16px')
        self.subject_le.setPlaceholderText(" 请输入邮件主题")
        self.subject_le.move(self.pos_x, self.subject.y()+self.subject.height())

        self.text = QLabel(main_window)
        self.text.resize(65, 25)
        self.text.setText('正文:')
        self.text.setStyleSheet('font-size:16px;font-weight:bold;font-family:SimHei')
        self.text.move(self.pos_x, self.subject_le.y()+self.subject_le.height())

        self.mail_text = QTextEdit(main_window)
        self.mail_text.setPlaceholderText(" 请输入邮件正文（字数限制在5000字内）")
        self.mail_text.setStyleSheet('font-size:16px')
        self.mail_text.resize(self.width, 430)
        self.mail_text.move(self.pos_x, self.text.y()+self.text.height())

        self.back_btn = QPushButton(main_window)
        self.back_btn.resize(90, 35)
        self.back_btn.move(745, 10)
        self.back_btn.setStyleSheet('background-color:white;font-size:16px;')
        self.back_btn.setText('返回')

        self.send_btn = QPushButton(main_window)
        self.send_btn.resize(90, 35)
        self.send_btn.move(650, 10)
        self.send_btn.setStyleSheet('background-color:white;font-size:16px;')
        self.send_btn.setText('发送')

    def update(self, account):
        self.sender_lb.setText(f'发件人: <{account}>')
        self.subject_le.setText('')
        self.receiver_le.setText('')
        self.mail_text.setText('')

    def show(self):
        self.state_slogan.show()
        self.sender_lb.show()
        self.receiver_lb.show()
        self.receiver_le.show()
        self.subject.show()
        self.subject_le.show()
        self.text.show()
        self.mail_text.show()
        self.back_btn.show()
        self.send_btn.show()

    def hide(self):
        self.state_slogan.hide()
        self.sender_lb.hide()
        self.receiver_lb.hide()
        self.receiver_le.hide()
        self.subject.hide()
        self.subject_le.hide()
        self.text.hide()
        self.mail_text.hide()
        self.back_btn.hide()
        self.send_btn.hide()
