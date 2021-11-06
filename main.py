import mailbox
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    my_mailbox = mailbox.Mailbox()
    my_mailbox.login_win.show()

    sys.exit(app.exec_())
