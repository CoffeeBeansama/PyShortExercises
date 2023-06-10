from win10toast import ToastNotifier
import psutil
import json
import smtplib
from urllib.request import urlopen
from datetime import datetime
from email.message import EmailMessage

class StartUp:

    def __init__(self):
        self.now = datetime.now()

        url = "http://ipinfo.io/json"
        response = urlopen(url)
        self.location_Data = json.load(response)
        self.toast = ToastNotifier()
        self.battery = psutil.sensors_battery()

        self.StartApp()

    def StartApp(self):

        self.sendMail("Sup",f"{self.now.hour.real}:{self.now.minute.real} \n "
                 f"{self.now.month.real}/{self.now.day.real}/{self.now.year.real} \n "
                 f"{self.location_Data}",
                 "Francisaigo12345@gmail.com")

        self.toast.show_toast(f"Welcome Aigo",
                               f"Battery percentage :  {self.battery.percent}% \n"
                               f"Power Plugged In :  {self.battery.power_plugged} \n"
                              , None, 30)


    def converTime(self,seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "%d:%02d:%02d" % (hours, minutes, seconds)
    def sendMail(self,subject,body,to):

        msg = EmailMessage()
        msg.set_content(body)
        msg["subject"] = subject
        msg["to"] = to

        user = "Francisaigo12345@gmail.com"
        msg["from"] = user
        password = "ydahcxzgdijjytyh"

        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(user=user,password=password)
        server.send_message(msg)
        server.quit()


    def convertTime(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "%d:%02d:%02d" % (hours, minutes, seconds)



startUp = StartUp()







