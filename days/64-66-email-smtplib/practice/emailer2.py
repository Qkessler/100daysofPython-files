import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


APP_PASSWORD = os.environ['APP_PASSWORD']
EMAIL = os.environ['EMAIL']


def send_email():
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = EMAIL
    msg['Subject'] = 'Test day 2'
    body = """This is the second day of coding emailing in python3

Today I will be including MIME to make better emails

    """
    msg.attach(MIMEText(body, 'plain'))
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(EMAIL, APP_PASSWORD)
    text = msg.as_string()
    smtp_server.sendmail(EMAIL, EMAIL, text)
    smtp_server.quit()
    print('Email sent successfully')


if __name__ == '__main__':
    send_email()
