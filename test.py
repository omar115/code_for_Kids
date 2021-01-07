import smtplib, ssl
from email.message import EmailMessage



msg = EmailMessage()

#y = int(input("How many mails do you want to send to Alauddin?"))

def mail(email, password, msg):
    port = 465

    smtpServer = 'smtp.gmail.com'
    
    with smtplib.SMTP_SSL(smtpServer, port) as server:
       server.login(email, password)
       server.send_message(msg)

for i in range(2):
    msg['To'] = input()
    msg['Subject'] = ''
    msg['Subject'] = input()
    k = input('body: ')
    msg.add_alternative(k)
    email = 'omarhasan115@gmail.com'
    msg['From'] = email
    password = 'elementary'
    mail(email, password, msg)
