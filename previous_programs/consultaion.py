import smtplib
import ssl
from email.message import EmailMessage

smtpserver = 'smtp.gmail.com'
port = 465
msg = EmailMessage()

msg['Subject'] = 'Test mail sent from a bot'
msg['From'] = ''     #sender
msg['To'] = ''       #receiver

email = 'omarhasan115@gmail.com'
password = input('pasword: ')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
    <body style="background-color:powderblue;">
    <body>
        <p>&#128512</p>
        <h1 style="color: purple">This is a test email sent from a python bot</h1>
        <h2 style="color: blue;">This is a small test</h2>
        <b> This is a HTML content based email </b>
        <i> Hello How are you??? </i>
        <p style="background-color:tomato;">
            <a href="http://www.omarHasan.com">Connect With me</a>
        </p>
        <button onclick="">HTML Tutorial</button>
    </body>
</html>
""", subtype = 'html')

with smtplib.SMTP_SSL(smtpserver, port) as s:
    s.login(email, password)
    s.send_message(msg)
