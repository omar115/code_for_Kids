'''
Note:
library install: pip install plyer

title: notification title
message: the message you want to give
app_icon: the icon you want to show
timeout: the duration of the notification that will show

'''
from plyer import notification
import time

i = 1
while i <= 10:
    notification.notify(
        title = 'Take a Break',
        message = 'Please take a break from your screen',
        app_icon = r'C:\Users\Ferntech\Desktop\git_workspace\code_for_Kids\automation_class\sample.ico',
        timeout = 15
    )
    

    
    time.sleep(2000)

    i = i + 1