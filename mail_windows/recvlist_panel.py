from PyQt5.QtWidgets import QListWidget, QLabel, QPushButton, QGroupBox, QAbstractItemView, QListWidgetItem
from PyQt5.QtCore import QStringListModel, QSize
from mail_windows import list_item


class RecvPanel:
    def __init__(self, main_window):
        self.state_slogan = QLabel(main_window)
        self.state_slogan.resize(500, 35)
        self.state_slogan.setText(f'   状态: 浏览收件箱中······')
        self.state_slogan.setStyleSheet('font-size:16px;font-weight:bold;font-family:SimHei;')
        self.state_slogan.move(10, 10)

        self.back_btn = QPushButton(main_window)
        self.back_btn.resize(90, 35)
        self.back_btn.move(745, 10)
        self.back_btn.setStyleSheet('background-color:white;font-size:16px;')
        self.back_btn.setText('返回')

        self.receiver = QGroupBox(main_window)
        self.receiver.setTitle('收件箱')
        self.receiver.resize(620, 580)
        self.receiver.move(214, 53)

        self.listmode = QStringListModel()

        self.mail_list = QListWidget(self.receiver)
        self.mail_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.mail_list.resize(590, 550)
        self.mail_list.move(15, 20)

    def update(self, subject, sender, time):
        item = QListWidgetItem()
        item.setSizeHint(QSize(560, 100))
        item_widget = list_item.ItemWidget(mail_subject=subject, mail_sender=sender, mail_time=time)
        self.mail_list.addItem(item)
        self.mail_list.setItemWidget(item, item_widget.item_widget)

    def hide(self):
        self.state_slogan.hide()
        self.back_btn.hide()
        self.receiver.hide()

    def show(self):
        self.state_slogan.show()
        self.back_btn.show()
        self.receiver.show()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QWidget
    app = QApplication(sys.argv)

    login_win = QWidget()
    login_win.setFixedSize(850, 650)
    recv = RecvPanel(login_win)

    login_win.show()

    sys.exit(app.exec_())
