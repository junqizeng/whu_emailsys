from PyQt5.QtWidgets import QWidget, QLabel


class ItemWidget:
    def __init__(self, mail_subject, mail_sender, mail_time):
        self.mail_subject = mail_subject
        self.mail_sender = mail_sender
        self.mail_sender = self.mail_sender.replace('<', '&lt;')
        self.mail_sender = self.mail_sender.replace('>', '&gt;')
        self.mail_date = mail_time

        self.item_widget = QWidget()

        self.subject_lb = QLabel(self.item_widget)
        self.subject_lb.setFixedSize(500, 33)
        self.subject_lb.setText('<font size=4> <font style="font-family:Microsoft YaHei"><b>'
                                f'{self.mail_subject}</b></font>')
        self.subject_lb.move(13, 7)

        self.sender_lb = QLabel(self.item_widget)
        self.sender_lb.setFixedSize(500, 20)
        self.sender_lb.setText('<font size=3><font color=grey> 发件人:&nbsp;&nbsp;'
                               f'{self.mail_sender}</font>')
        self.sender_lb.move(13, self.subject_lb.y()+self.subject_lb.height())

        self.time_lb = QLabel(self.item_widget)
        self.time_lb.setFixedSize(500, 20)
        self.time_lb.setText('<font size=3><font color=grey> 时&nbsp;&nbsp;&nbsp;&nbsp;间:&nbsp;&nbsp;'
                             f'{self.mail_date}</font>')
        self.time_lb.move(self.sender_lb.x(), self.sender_lb.y()+self.sender_lb.height()+2)
