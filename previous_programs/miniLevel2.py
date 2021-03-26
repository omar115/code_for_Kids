import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'omarhasan115@gmail.com'
EMAIL_PASSWORD = 'elementary'


msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'omarhasan115@gmail.com'


msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <b>This is an HTML Email!</b>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
