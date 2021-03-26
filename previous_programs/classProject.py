import smtplib, ssl

port = 465

smtpServer = 'smtp.gmail.com'
sender = 'omarhasan115@gmail.com'
receiver = 'zabeer.omar07@gmail.com'
password = input('enter your password here')

message = """\
        
Subject: Python Consultation Hour
Please Do Active on 7.00 PM Tomorrow, Thank you"""


context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtpServer, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)