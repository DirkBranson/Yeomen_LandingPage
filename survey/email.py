# myapp/utils.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(content):
    sender_email = "survey@yeomen.co.uk"
    receiver_email = "info@yeomen.co.uk"
    smtp_password = "glenf4rcl4s"  # Use environment variable or safer method in production
    smtp_username = "yeomen.co.uk"  # Use environment variable or safer method in production

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'New Survey Submission'
    message.attach(MIMEText(content, 'plain'))

    #server = smtplib.SMTP('mail.smtp2go.com', 2525)
    #server.starttls()
    #server.login(smtp_username, smtp_password)
    #text = message.as_string()
    #server.sendmail(sender_email, receiver_email, text)
    #server.quit()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("dunnettjalex@gmail.com", "rios opgh iiat cvsz")
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()