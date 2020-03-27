import smtplib
import os

APP_PASSWORD = os.environ['APP_PASSWORD']
EMAIL = os.environ['EMAIL']


def send_email():
    from_addr = EMAIL
    to_addr = EMAIL
    body = """This is a test

    This is the body for the test

    """
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(EMAIL, APP_PASSWORD)
    smtp_server.sendmail(from_addr, to_addr, body)
    smtp_server.quit()
    print('Email sent successfully')


if __name__ == '__main__':
    send_email()
