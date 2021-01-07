import smtplib
import ssl
from email.message import EmailMessage

smtpserver = 'smtp.gmail.com'
port = 465

msg = EmailMessage()

msg['Subject'] = 'Email sent from the bot'
#from means sender, to means receiver
msg['From'] = 'omarhasan115@gmail.com'
msg['To'] = 'coderayman07@gmail.com'

email = 'omarhasan115@gmail.com'
password = input('give your password here: ')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <b>This is an <i>HTML</i> Email!</b>
        <p>
            <a href="http://www.google.com">Search ON Google</a>
        </p>
    </body>
</html>
""", subtype = 'html')

with smtplib.SMTP_SSL(smtpserver,port) as server:
    server.login(email, password)
    server.send_message(msg)
    
