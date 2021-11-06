from mail_procotols import smpt
from mail_procotols import pop3
from email.parser import Parser
from email.utils import parseaddr
from datetime import datetime
from email.header import decode_header
from PyQt5.QtWidgets import QMessageBox


def pop_message(win, title, report, icon):
    message_box = QMessageBox(win)
    message_box.setWindowTitle(title)
    if '\n' in report:
        login_report = report.split('\n')
        message_box.setText('<h3>%s</h3>' % login_report[0])
        message_box.setInformativeText(login_report[1])
    else:
        message_box.setText('<h3>%s</h3>' % report)
    message_box.setIcon(icon)
    return message_box


def get_body(msg):  # 处理邮件正文
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        # print(msg)
        # print(msg.get('Content-Type'))
        return msg.get('Content-Type'), msg.get_payload(None, decode=True)


def decode_str(s):  # 字符编码转换
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def process_mail_basic(mail_content):
    mail = {}
    mail_content = b'\r\n'.join(mail_content).decode('utf-8')
    mail_content = Parser().parsestr(mail_content)
    # print(mail_content)

    mail_subject = mail_content.get('Subject')
    mail_subject = decode_str(mail_subject)

    mail_time = decode_header(mail_content.get('date'))
    mail_time = mail_time[0][0]
    try:
        mail_time_data = datetime.strptime(str(mail_time[5:24]), '%d %b %Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
        mail_time = f'{mail_time_data} {str(mail_time[25:36])}'
    except:
        mail_time = str(mail_time[5:24])

    hdr, addr = parseaddr(mail_content.get('From'))
    mail_sender, charset = decode_header(hdr)[0]
    if charset:
        mail_sender = mail_sender.decode(charset)
    mail_sender = u'%s <%s>' % (mail_sender, addr)

    mail['subject'] = mail_subject
    mail['sender'] = mail_sender
    mail['time'] = mail_time
    return mail


def process_mail(mail_content, mail_acc):
    mail = {}
    mail_content = b'\r\n'.join(mail_content).decode('utf-8')
    mail_content = Parser().parsestr(mail_content)
    # print(mail_content)

    mail_subject = mail_content.get('Subject')
    mail_subject = decode_str(mail_subject)

    import chardet
    text_charset, mail_text = get_body(mail_content)
    # print(text_charset, mail_text)
    guess_charset = chardet.detect(mail_text)

    try:
        text_charset = text_charset.split(';')[1]
        text_charset = text_charset.split('charset=')[-1]
        mail_text = mail_text.decode(text_charset)
    except:
        mail_text = mail_text.decode(guess_charset['encoding'])
        # print(guess_charset)

    # mail_text = base64.b64decode(mail_text)

    mail_time = decode_header(mail_content.get('date'))
    mail_time = mail_time[0][0]
    mail_time_data = datetime.strptime(str(mail_time[5:24]), '%d %b %Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
    mail_time = f'{mail_time_data} {str(mail_time[25:36])}'

    hdr, addr = parseaddr(mail_content.get('From'))
    mail_sender, charset = decode_header(hdr)[0]
    if charset:
        mail_sender = mail_sender.decode(charset)
    mail_sender = u'%s <%s>' % (mail_sender, addr)

    mail['subject'] = mail_subject
    mail['text'] = mail_text
    mail['sender'] = mail_sender
    mail['time'] = mail_time
    mail['receiver'] = mail_acc
    return mail


class MailToolkit:
    def __init__(self):
        self.client_smtp = None
        self.client_pop = None

    def mail_login(self, acc_mail, account, author_code):
        self.client_smtp = smpt.SMTP(acc_mail, account=account, author_code=author_code)
        self.client_pop = pop3.POP3(acc_mail=acc_mail, account=account, author_code=author_code)
        smtp_login, smtp_report, smpt_socket = self.client_smtp.login_veri()
        if not smtp_login:
            return False, smtp_report
        smpt_socket.sendall(self.client_smtp.smtp_command['QUIT'])

        pop_login, pop_report, pop_socket = self.client_pop.login_veri()
        if not smtp_login:
            return False, pop_report
        pop_socket.sendall(self.client_pop.pop_command['QUIT'])

        return True, 'SMTP/POP3服务认证成功！'

    # def mail_write(self):

    def mail_send(self, receiver, subject, message):
        login_flag, _, smpt_socket = self.client_smtp.login_veri()
        if not login_flag:
            return False, '发送失败！\nSMTP服务连接中断！'

        send_flag, send_report = self.client_smtp.mail_send(
            receiver=receiver, subject=subject, message=message, client_socket=smpt_socket
        )

        return send_flag, send_report

    def mail_read(self, mail_index):
        login_flag, _, pop_socket = self.client_pop.login_veri()
        if not login_flag:
            return False, '邮件读取失败！\nPOP服务连接中断！'

        read_flag, read_report = self.client_pop.mail_read(mail_index=mail_index)

        return read_flag, read_report

    def mail_dele(self, dele_num=-1):
        login_flag, _, pop_socket = self.client_pop.login_veri()
        if not login_flag:
            return False, '删除失败！\nPOP服务连接中断！'

        dele_flag, dele_report = self.client_pop.mail_dele(dele_num=dele_num, client_socket=pop_socket)
        return dele_flag, dele_report

    def mail_list(self):
        login_flag, _, pop_socket = self.client_pop.login_veri()
        if not login_flag:
            return False, '查询失败！\nPOP服务连接中断！'

        list_flag, list_report = self.client_pop.mail_list(pop_socket)
        return list_flag, list_report

    def mail_stats(self):
        login_flag, _, pop_socket = self.client_pop.login_veri()
        if not login_flag:
            return False, '查询失败\nPOP服务连接中断！'

        stats_flag, stats_report = self.client_pop.mail_stats(pop_socket)
        return stats_flag, stats_report

    def mail_read_all(self):
        stats_flag, stats_report = self.mail_stats()
        if not stats_flag:
            return False, '列表显示失败！\nPOP服务连接中断！'
        mail_num = stats_report.split(' ')[1]
        read_flag, read_report = self.client_pop.mail_read_all(mail_num)

        return read_flag, read_report
