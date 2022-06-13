from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class Email(object):
    _instance = None
    _sender_address = None
    _sender_pass = None

    def __init__(self):
        self._sender_address = "joey.cm.lam@gmail.com"
        self._sender_pass = 'xxxxxx'

    def sendEmail(self, recipents, msg):
        receiver_address = recipents
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = self._sender_address
        message['To'] = receiver_address
        message['Subject'] = 'A test mail sent by Python.'  # The subject line
        # The body and the attachments for the mail
        # message.attach(MIMEText(mail_content, 'plain'))
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(self._sender_address, self._sender_pass)  # login with mail_id and password
        session.sendmail(self._sender_address, receiver_address, msg)
        session.quit()

