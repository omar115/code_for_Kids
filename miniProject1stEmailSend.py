import smtplib, ssl

port = 465

smtpServer = 'smtp.gmail.com'
sender = 'omarhasan115@gmail.com'
receiver = 'omarhasan115@gmail.com'
password = input('pass: ')

x='sdfad'
y='adjf'
msg = """\
Subject: """+x+"""

"""+y


context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtpServer, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg)