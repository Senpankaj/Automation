import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# Email account credentials
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
IMAP_SERVER = 'imap.example.com'
IMAP_PORT = 993
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SPECIFIC_SENDER = 'specific_sender@example.com'
AUTO_REPLY_SUBJECT = 'Your Custom Subject Here'

def check_email():
    # Connect to the email server
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    mail.select('inbox')

    # Search for emails from the specific sender
    result, data = mail.search(None, f'(FROM "{SPECIFIC_SENDER}")')

    if result == 'OK':
        for num in data[0].split():
            result, msg_data = mail.fetch(num, '(RFC822)')
            if result == 'OK':
                msg = email.message_from_bytes(msg_data[0][1])

                # Check if the email is unread
                if 'UNSEEN' in mail.fetch(num, '(FLAGS)')[1][0].decode():
                    send_auto_reply(msg)

    mail.logout()

def send_auto_reply(original_msg):
    # Create the email
    reply = MIMEMultipart()
    reply['From'] = EMAIL_ADDRESS
    reply['To'] = SPECIFIC_SENDER
    reply['Subject'] = AUTO_REPLY_SUBJECT

    # Create the body of the email
    body = "This is an automated response to your email."
    reply.attach(MIMEText(body, 'plain'))

    # Send the email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, SPECIFIC_SENDER, reply.as_string())

if __name__ == '__main__':
    check_email()