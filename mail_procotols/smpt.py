from socket import *
from base64 import *

smtp_sever = {
    '@163.com': 'smtp.163.com',
    '@whu.edu.cn': 'smtp.whu.edu.cn',
    '@qq.com': 'smtp.qq.com',
}

smtp_port = {
    '@163.com': 25,
    '@whu.edu.cn': 25,
    '@qq.com': 25
}


class SMTP:
    def __init__(self, acc_mail, account, author_code):
        self.smtp_sever = smtp_sever[acc_mail]
        self.smtp_port = smtp_port[acc_mail]
        self.acc_mail = acc_mail
        self.account = account
        self.author_code = author_code

        self.smtp_command = {
            'HELO': 'HELO world\r\n'.encode(),
            'LOGIN': 'AUTH LOGIN\r\n'.encode(),
            'account': b64encode(f'{self.account}'.encode()) + '\r\n'.encode(),
            'author_code': b64encode(f'{self.author_code}'.encode()) + '\r\n'.encode(),
            'sender_addr': f'MAIL FROM: <{self.account}{self.acc_mail}>\r\n'.encode(),
            'DATA': f'DATA\r\n'.encode(),
            'end': '\r\n.\r\n'.encode(),
            'QUIT': 'QUIT\r\n'.encode(),
        }

    def login_veri(self):
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((self.smtp_sever, self.smtp_port))
        recv_mes = client_socket.recv(1024).decode()
        if not recv_mes[:3] == '220':
            return False, "SMTP服务器连接失败！\n请检查网络设置！", None

        client_socket.sendall(self.smtp_command['HELO'])
        recv_mes = client_socket.recv(1024).decode()
        if not recv_mes[:3] == '250':
            return False, "SMTP服务器连接中断！\n请检查网络设置！", None

        client_socket.sendall(self.smtp_command['LOGIN'])
        recv_mes = client_socket.recv(1024).decode()
        if not recv_mes[:3] == '334':
            return False, "SMTP服务器连接中断！\n请检查网络设置！", None

        client_socket.sendall(self.smtp_command['account'])
        recv_mes = client_socket.recv(1024).decode()
        if not recv_mes[:3] == '334':
            return False, "SMTP服务器认证失败！\n用户不存在，请检查邮箱账号！", None

        client_socket.sendall(self.smtp_command['author_code'])
        recv_mes = client_socket.recv(1024).decode()
        if not recv_mes[:3] == '235':
            return False, "SMTP服务器认证失败！\n授权码错误，请检查授权码！", None

        return True, '认证成功！', client_socket

    def mail_send(self, receiver, subject, message, client_socket):
        client_socket.sendall(self.smtp_command['sender_addr'])
        recv_mes = client_socket.recv(1024).decode()

        if not recv_mes[:3] == '250':
            return False, "发送方设置失败！\n请重试！"

        receiver_command = f'RCPT TO: <{receiver}>\r\n'.encode()
        client_socket.sendall(receiver_command)
        recv_mes = client_socket.recv(1024).decode()
        if not recv_mes[:3] == '250':
            return False, "接收方设置失败！\n请重试！"

        client_socket.sendall(self.smtp_command['DATA'])
        recv_mes = client_socket.recv(1024).decode()
        if not recv_mes[:3] == '354':
            return False, "发送失败！\n请重试！"

        mail = {
            'from': f'from:<{self.account}{self.acc_mail}>\r\n',
            'to': f'to:<{receiver}>\r\n',
            'subject': f'subject:{subject}\r\n',
            'text': f"\r\n{message}",
        }
        mail['content'] = (
                mail['from'] + mail['to'] + mail['subject'] + mail['text']).encode()

        client_socket.sendall(mail['content'])

        client_socket.sendall(self.smtp_command['end'])
        recv_mes = client_socket.recv(1024).decode()
        if not recv_mes[:3] == '250':
            return False, "发送未正常结束！\n请重试！"

        client_socket.sendall(self.smtp_command['QUIT'])
        return True, "发送成功！\n对方很快就会看到！"
