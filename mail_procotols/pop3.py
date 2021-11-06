from socket import *
import poplib
from mail_procotols import mailtoolkit


pop3_sever = {
    '@163.com': 'pop.163.com',
    '@whu.edu.cn': 'whu.edu.cn',
    '@qq.com': 'pop.qq.com'
}

pop3_port = {
    '@163.com': 110,
    '@whu.edu.cn': 110,
    '@qq.com': 110
}


class POP3:
    def __init__(self, acc_mail, account, author_code):
        self.pop_server = pop3_sever[acc_mail]
        self.pop_port = pop3_port[acc_mail]
        self.acc_mail = acc_mail
        self.account = account
        self.author_code = author_code
        self.pop_command = {
            'USER': f'USER {self.account}{self.acc_mail}\r\n'.encode(),
            'PASS': f'PASS {self.author_code}\r\n'.encode(),
            'STAT': 'STAT\r\n'.encode(),
            'LIST': 'LIST\r\n'.encode(),
            'QUIT': 'QUIT\r\n'.encode(),
        }

    def login_veri(self):
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((self.pop_server, self.pop_port))
        recv_mes = client_socket.recv(1024).decode()
        if not recv_mes[:3] == '+OK':
            return False, "POP3服务器连接失败！\n请检查网络设置！", None

        client_socket.sendall(self.pop_command['USER'])
        recv_mes = client_socket.recv(1024).decode()
        if not recv_mes[:3] == '+OK':
            return False, "SMTP服务器认证失败，用户不存在！\n请检查网络设置或邮箱账号！", None

        client_socket.sendall(self.pop_command['PASS'])
        recv_mes = client_socket.recv(1024).decode()
        if not recv_mes[:3] == '+OK':
            return False, "SMTP服务器认证失败，用户不存在！\n请检查网络设置或邮箱账号！", None

        # client_socket.sendall(pop_command['QUIT'])
        return True, '登录认证成功!', client_socket

    def mail_stats(self, client_socket):
        client_socket.sendall(self.pop_command['STAT'])
        recv_mes = client_socket.recv(1024).decode()
        if not recv_mes[:3] == '+OK':
            return False, "邮件统计失败！\n请检查网络设置！"

        client_socket.sendall(self.pop_command['QUIT'])
        return True, recv_mes

    def mail_list(self, client_socket):
        client_socket.sendall(self.pop_command['LIST'])
        recv_mes = client_socket.recv(1024).decode()
        if not recv_mes[:3] == '+OK':
            return False, "邮件列表更新失败！\n请检查网络设置！"

        return True, recv_mes

    def mail_read(self, mail_index):
        mail_content = None

        client_pop = poplib.POP3(self.pop_server)
        client_pop.set_debuglevel(1)
        client_pop.user(self.account)
        client_pop.pass_(self.author_code)
        print("Messages: %s Size: %s" % (client_pop.stat()))
        _, mail_content, _ = client_pop.retr(mail_index)
        if mail_content is None:
            return False, '邮件内容获取失败！\n请检查网络设置！'
        # print(mail_content)
        if self.acc_mail != '@whu.edu.cn':
            client_pop.quit()
        return True, mail_content

    def mail_dele(self, dele_num, client_socket):

        dele_command = f'DELE {dele_num}\r\n'.encode()
        client_socket.sendall(dele_command)
        recv_mes = client_socket.recv(1024).decode()
        if not recv_mes[:3] == '+OK':
            return False, "邮件删除失败！\n请检查网络设置！"

        client_socket.sendall(self.pop_command['QUIT'])
        return True, '邮件删除成功！\n'

    def mail_read_all(self, mail_num):
        all_mail = ''

        client_pop = poplib.POP3(self.pop_server)
        client_pop.set_debuglevel(1)
        client_pop.user(self.account)
        client_pop.pass_(self.author_code)
        for i in range(1, int(mail_num)+1):
            _, mail_content, _ = client_pop.retr(i)
            if mail_content is None:
                return False, '邮件内容获取失败！\n请检查网络设置！'
            mail = mailtoolkit.process_mail_basic(mail_content)
            all_mail = all_mail + '%s^>%s^>%s,' % (mail['subject'], mail['sender'], mail['time'])
        if self.acc_mail != '@whu.edu.cn':
            client_pop.quit()
        return True, all_mail


if __name__ == '__main__':
    mail_index = 1
    acc_mail = '@whu.edu.cn'
    account = ''
    author_code = ''
    clinet_pop = POP3(acc_mail=acc_mail, account=account, author_code=author_code)
    _, mail = clinet_pop.mail_read(mail_index=mail_index)
    mail = mailtoolkit.process_mail(mail, mail_acc=account)
    print(mail)
