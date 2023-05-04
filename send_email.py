# Import modules.
import smtplib, ssl
import os
def send_email(message):
    """
    1. Get username & app password for my google account.
    2. Get the SMTP host and SSL port for google.com
    3. add context variable using ssl.create_default_context()
    4. Create smtplib server, login using credentials, send email.
    """
    username = 'keshawn936@gmail.com'
    password = os.getenv('PASSWORD')

    receiver = 'keshawn936@gmail.com'
    Host = 'smtp.google.com'

    Port = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(Host, Port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
