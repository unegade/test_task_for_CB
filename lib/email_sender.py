from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase
from email import encoders
import smtplib


class EmailSender():
    def __init__(self, mail: str, password, mptpServer='smtp.yandex.ru', smtpPort=465):
        self.mail = mail
        self.login = mail.split('@')[0]
        self.password = password
        self.server = smtplib.SMTP_SSL(mptpServer, smtpPort)

    def send_mail(self, to, subject, body, image_attach: dict = {}):
        try:
            self.server.connect('smtp.yandex.ru', 465)
            self.server.login(self.login, self.password)
            message = MIMEMultipart("alternative")
            message["Subject"] = subject
            message["From"] = self.mail
            message["To"] = to
            message.attach((MIMEText(body, 'plain')))
            for name, file in image_attach.items():
                attach = MIMEBase('application', 'octet-stream')
                attach.set_payload(file)
                encoders.encode_base64(attach)
                attach.add_header('Content-Disposition', "attachment; filename={}.png".format(name))
                message.attach(attach)
            self.server.sendmail(self.mail, to, message.as_string())
            self.server.quit()
        except:
            raise Exception('Ошибка отправки сообщения')
