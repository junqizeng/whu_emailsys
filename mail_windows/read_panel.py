from PyQt5.QtWidgets import QLabel, QTextEdit, QPushButton

# from mail_procotols import pop3


class ReadPanel:
    def __init__(self, main_window):
        self.pos_x = 214
        self.width = 620

        self.state_slogan = QLabel(main_window)
        self.state_slogan.resize(500, 35)
        self.state_slogan.setText(f'   状态: 阅读邮件中······')
        self.state_slogan.setStyleSheet('font-size:16px;font-weight:bold;font-family:SimHei;')
        self.state_slogan.move(10, 10)

        self.subject_lb = QLabel(main_window)
        self.subject_lb.resize(600, 25)
        self.subject_lb.setStyleSheet('font-size:22px;font-weight:bold;font-family:SimHei')
        self.subject_lb.move(self.pos_x, 50)

        self.sender_lb = QLabel(main_window)
        self.sender_lb.resize(600, 25)
        self.sender_lb.setStyleSheet('font-size:16px;font-family:SimHei;color:grey')
        self.sender_lb.move(self.pos_x, self.subject_lb.y()+self.subject_lb.height())

        self.time_lb = QLabel(main_window)
        self.time_lb.resize(600, 25)
        self.time_lb.setStyleSheet('font-size:16px;font-family:SimHei;color:grey')
        self.time_lb.move(self.pos_x, self.sender_lb.y()+self.sender_lb.height())

        self.receiver_lb = QLabel(main_window)
        self.receiver_lb.resize(600, 25)
        self.receiver_lb.setStyleSheet('font-size:16px;font-family:SimHei;color:grey')
        self.receiver_lb.move(self.pos_x, self.time_lb.y()+self.time_lb.height())

        self.text_lb = QLabel(main_window)
        self.text_lb.resize(65, 25)
        self.text_lb.setText('正文:')
        self.text_lb.setStyleSheet('font-size:16px;font-family:SimHei;color:grey')
        self.text_lb.move(self.pos_x, self.receiver_lb.y()+self.receiver_lb.height())

        self.text_tx = QTextEdit(main_window)
        self.text_tx.setStyleSheet('font-size:16px')
        self.text_tx.resize(self.width, 450)
        self.text_tx.setReadOnly(True)
        self.text_tx.move(self.pos_x, self.text_lb.y()+self.text_lb.height())

        self.back_btn = QPushButton(main_window)
        self.back_btn.resize(90, 35)
        self.back_btn.move(745, 10)
        self.back_btn.setStyleSheet('background-color:white;font-size:16px;')
        self.back_btn.setText('返回')

        self.delete_btn = QPushButton(main_window)
        self.delete_btn.resize(90, 35)
        self.delete_btn.setStyleSheet('background-color:white;font-size:16px;')
        self.delete_btn.move(650, 10)
        self.delete_btn.setText('删除')

    def update(self, mail):

        mail_subject = mail['subject']
        mail_sender = mail['sender']
        mail_receiver = mail['receiver']
        mail_text = mail['text']
        mail_time = mail['time']

        self.subject_lb.setText(f'{mail_subject}')
        self.sender_lb.setText(f'发件人: {mail_sender}')
        self.time_lb.setText(f'时  间: {mail_time}')
        self.receiver_lb.setText(f'收件人: <{mail_receiver}>')
        self.text_tx.setText(mail_text)

    def hide(self):
        self.state_slogan.hide()
        self.subject_lb.hide()
        self.sender_lb.hide()
        self.time_lb.hide()
        self.receiver_lb.hide()
        self.text_lb.hide()
        self.text_tx.hide()
        self.back_btn.hide()
        self.delete_btn.hide()

    def show(self):
        self.state_slogan.show()
        self.subject_lb.show()
        self.sender_lb.show()
        self.time_lb.show()
        self.receiver_lb.show()
        self.text_lb.show()
        self.text_tx.show()
        self.back_btn.show()
        self.delete_btn.show()


# if __name__ == '__main__':

    # read_num =
    # acc_mail =
    # account =
    # author_code =
    # clinet_pop = pop3.POP3(acc_mail=acc_mail, account=account, author_code=author_code)
    # mail = clinet_pop.mail_read(read_num=read_num)
    # import sys
    # from PyQt5.QtWidgets import QApplication, QWidget
    # app = QApplication(sys.argv)
    # login_win = QWidget()
    # login_win.setFixedSize(850, 650)
    # recv = ReadPanel(login_win)
    # recv.update(mail)
    #
    # login_win.show()
    #
    # sys.exit(app.exec_())
