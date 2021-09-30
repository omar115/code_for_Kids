from plyer import notification
import time

while True:
    notification.notify(
        title= "take a break",
        message= "please take a break from your screen",
        app_icon= r"C:\Users\USER\Desktop\python\Automation class\Reminderappp\bell.ico" ,
        timeout= 20
    )

    time.sleep(3600)