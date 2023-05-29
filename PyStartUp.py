from win10toast import ToastNotifier
import psutil


def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


# returns a tuple
battery = psutil.sensors_battery()


toast = ToastNotifier()
toast.show_toast("Welcome Aigo",f"Battery percentage :  {battery.percent}%",None,30)



