import smtplib
import ssl
from email.message import EmailMessage

smtpserver = 'smtp.gmail.com'
port = 465
msg = EmailMessage()

msg['Subject'] = 'Happy New Year from Python Team'
msg['From'] = 'omarhasan115@gmail.com'     #sender
msg['To'] = 'asuername@gmail.com'       #receiver

email = 'omarhasan115@gmail.com'
password = 'elementary'

msg.add_alternative("""\
<!DOCTYPE html>
<html>
<head>
</head>
    <body style="background-color:#FFFAFA">
    <body>
        <h1 style="color: purple"><p>---------------------------------------Happy New Year 2021-----------------------------</p></h1>
        <h2 style="color:#FFA500;">
             Hello little warriors! In 2020, you saw a different world. Kudos to you that you fought and still fighting.
            InshaAllah, we pray that in <i><b>2021</b></i> everything will be okay.
        </h2>
        <h3 style="color:#008080">Welcome 2021!
        </h3>
        <h4 style = "color: #A52A2A">
             <b>Stay at home and happy <i>coding</i></b> :-)
        </h4>
    </body>
</html>
""", subtype = 'html')

with smtplib.SMTP_SSL(smtpserver, port) as s:
    s.login(email, password)
    s.send_message(msg)
