from os import getenv
from smtplib import SMTPException
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_hash(email: str, hash: str):
    # https://www.tutorialspoint.com/send-mail-from-your-gmail-account-using-python
    mail_content = '<button value="' + hash + '"></button>'
    message = MIMEMultipart()
    message['From'] = getenv('MAIL_SENDER')
    message['To'] = email
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'

    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'html'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(getenv('MAIL_SENDER'), getenv('MAIL_PASS'))
    text = message.as_string()
    session.sendmail(getenv('MAIL_SENDER'), email, text)
    session.quit()
    print('Mail sent')
