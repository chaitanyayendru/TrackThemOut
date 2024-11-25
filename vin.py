import psutil
# battery = psutil.sensors_battery()
# print("Battery:", battery)

from win10toast import ToastNotifier

battery = psutil.sensors_battery()
percent = battery.percent
plugged = battery.power_plugged
toast = ToastNotifier()

if percent >= 85 and plugged:
    print(f"Battery at {percent}%. Notification triggered.")
    toast.show_toast(
        "Battery Full Alert",
        f"Battery is at {percent}%. Please unplug your charger.",
        duration=10,
        threaded=True
    )