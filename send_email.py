from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#MAILER_URL = "smtp.mailtrap.io"
MAILER_URL = "localhost"
#SMTP_LOGIN_USER = "xxxxxxxxxx"
#SMTP_LOGIN_PASSWORD = "xxxxxxxxx"


def send_mail(sender, receiver, subject, body):
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
  
    msg.attach(MIMEText(body, 'html'))
  
    with smtplib.SMTP(MAILER_URL, 25) as server:
        #server.login(SMTP_LOGIN_USER, SMTP_LOGIN_PASSWORD)
        server.sendmail(sender, receiver, msg.as_string())\

if __name__ == "__main__":
    send_mail(
        sender="noreply@somewhere.com",
        receiver="somebody@somewhere.com",
        subject="Test Python Mailing",
        body="<h3>Hello, this is an automated email!</h3>"
    )
