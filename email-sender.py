# Please turn on less secure app access for your gmail account when using this

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def main():
    ADDRESS = '<your_id>@gmail.com'
    PASSWORD = '<your_password>'
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(ADDRESS, PASSWORD)
    msg = MIMEMultipart()
    msg['From'] = ADDRESS
    msg['To'] = '<receiver_address>@gmail.com'
    msg['Subject'] = 'Test Run'
    msg.attach(MIMEText('<some message here>', 'plain'))

    s.send_message(msg)
    del msg
    s.quit() # Don't forget to quit the session!
    

main()
