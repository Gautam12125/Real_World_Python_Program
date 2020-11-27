import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
        title = "**Please Drink Water Now!**",
        message ='''You've probably heard the advice to drink eight glasses of water a day. 
        That's easy to remember, and it's a reasonable goal.''',
        app_icon="icons/Iconsmind-Outline-Glass-Water.ico",
        timeout=2
        )
        time.sleep(2*6)