from PyQt5.QtWidgets import QApplication, QMessageBox, QPushButton
from mail_procotols import mailtoolkit
from mail_windows import client_window, login_window, read_panel, recvlist_panel, write_panel, wel_panel


class Mailbox:
    def __init__(self):
        self.mail_acc = ''
        self.mail_type = ''
        self.mail_pwd = ''
        self.mail_index = -1

        self.mail_toolkit = mailtoolkit.MailToolkit()

        self.login_win = login_window.LoginWindow()
        self.login_win.login_btn.clicked.connect(self.login_to_client)

        self.client_win = client_window.ClientWindow()
        self.client_win.write_btn.clicked.connect(self.jump_to_write)
        self.client_win.receiver_btn.clicked.connect(self.jump_to_recv)

        self.wel_panel = wel_panel.WelPanel(self.client_win)

        self.read_panel = read_panel.ReadPanel(self.client_win)
        self.read_panel.back_btn.clicked.connect(self.jump_to_recv)
        self.read_panel.delete_btn.clicked.connect(self.jump_to_delete)

        self.recvlist_panel = recvlist_panel.RecvPanel(self.client_win)
        self.recvlist_panel.back_btn.clicked.connect(self.jump_to_client)
        self.recvlist_panel.mail_list.doubleClicked.connect(self.jump_to_read)

        self.write_panel = write_panel.WritePanel(self.client_win)
        self.write_panel.send_btn.clicked.connect(self.send_email)
        self.write_panel.back_btn.clicked.connect(self.jump_to_client)

        self.wel_panel.hide()
        self.read_panel.hide()
        self.write_panel.hide()
        self.recvlist_panel.hide()

    def login_to_client(self):
        self.mail_acc = self.login_win.account_le.text()
        self.mail_pwd = self.login_win.pwd_le.text()
        self.mail_type = self.login_win.mail_choice.currentText()

        login_flag, login_report = self.mail_toolkit.mail_login(
            acc_mail=self.mail_type, account=self.mail_acc, author_code=self.mail_pwd)
        if not login_flag:
            login_message = mailtoolkit.pop_message(
                win=self.login_win, title='登陆失败', icon=QMessageBox.Critical, report=login_report)
            login_message.show()
            return
        stats_flag, stats_report = self.mail_toolkit.mail_stats()
        if not stats_flag:
            login_message = mailtoolkit.pop_message(
                win=self.login_win, title='登陆失败', icon=QMessageBox.Critical, report=login_report)
            login_message.show()
            return
        self.wel_panel.update(mail_acc=self.mail_acc, mail_stats=stats_report)
        self.login_win.hide()
        self.client_win.show()
        self.wel_panel.show()

    def jump_to_write(self):
        self.write_panel.update(self.mail_acc + self.mail_type)
        self.wel_panel.hide()
        self.read_panel.hide()
        self.recvlist_panel.hide()
        self.write_panel.show()

    def jump_to_recv(self):
        self.wel_panel.hide()
        self.write_panel.hide()
        self.read_panel.hide()
        self.list_mail()
        self.recvlist_panel.show()

    def jump_to_client(self):
        stats_flag, stats_report = self.mail_toolkit.mail_stats()
        if not stats_flag:
            login_message = mailtoolkit.pop_message(
                win=self.client_win, title='错误', icon=QMessageBox.Critical, report=stats_report)
            login_message.show()
            return
        self.wel_panel.update(mail_acc=self.mail_acc, mail_stats=stats_report)
        self.write_panel.hide()
        self.recvlist_panel.hide()
        self.read_panel.hide()
        self.wel_panel.show()

    def jump_to_read(self, index):
        self.mail_index = int(index.row()) + 1
        read_flag, read_report = self.mail_toolkit.mail_read(mail_index=self.mail_index)
        if not read_flag:
            login_message = mailtoolkit.pop_message(
                win=self.client_win, title='错误', icon=QMessageBox.Critical, report='错误\n连接中断')
            login_message.show()
            return

        mail = mailtoolkit.process_mail(mail_content=read_report, mail_acc=self.mail_acc + self.mail_type)
        self.wel_panel.hide()
        self.write_panel.hide()
        self.recvlist_panel.hide()
        self.read_panel.update(mail)
        self.read_panel.show()

    def jump_to_delete(self):
        confirm_message = mailtoolkit.pop_message(
            win=self.client_win, title='删除确认', icon=QMessageBox.Question, report='确定要删除邮件吗？\n删除后可能无法恢复')
        confirm_message.addButton(QPushButton('确定删除', confirm_message), QMessageBox.YesRole)
        confirm_message.addButton(QPushButton('取消', confirm_message), QMessageBox.NoRole)
        confirm_message.show()

        def delete_mail(btn):
            btn_role = QMessageBox.buttonRole(confirm_message, btn)
            if btn_role == QMessageBox.YesRole:
                delete_flag, delete_report = self.mail_toolkit.mail_dele(self.mail_index)
                if not delete_flag:
                    delete_message = mailtoolkit.pop_message(
                        win=self.client_win, title='删除失败', icon=QMessageBox.Critical, report=delete_report)
                    delete_message.show()
                else:
                    self.jump_to_recv()
                    delete_message = mailtoolkit.pop_message(
                        win=self.client_win, title='删除成功', icon=QMessageBox.Information, report=delete_report)
                    delete_message.show()

        confirm_message.buttonClicked.connect(delete_mail)

    def send_email(self):
        mail_subject = self.write_panel.subject_le.text()
        mail_receiver = self.write_panel.receiver_le.text()
        mail_text = self.write_panel.mail_text.toPlainText()
        send_flag, send_report = self.mail_toolkit.mail_send(
            receiver=mail_receiver, subject=mail_subject, message=mail_text)
        if not send_flag:
            send_message = mailtoolkit.pop_message(
                win=self.client_win, title='错误', icon=QMessageBox.Critical, report=send_report)
            send_message.show()
        else:
            send_message = mailtoolkit.pop_message(
                win=self.client_win, title='成功', icon=QMessageBox.Information, report=send_report)
            send_message.show()

    def list_mail(self):
        self.recvlist_panel.mail_list.clear()
        list_flag, list_report = self.mail_toolkit.mail_read_all()
        if not list_flag:
            login_message = mailtoolkit.pop_message(
                win=self.client_win, title='错误', icon=QMessageBox.Critical, report=list_report)
            login_message.show()
            return
        mails = list_report[:-1].split(',')
        i = 0
        for mail in mails:
            mail = mail.split('^>')
            self.recvlist_panel.update(subject=mail[0], sender=mail[1], time=mail[2])
            i += 1
