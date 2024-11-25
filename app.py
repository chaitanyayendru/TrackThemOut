import time
import psutil
import json
import os
from threading import Thread
from tkinter import Tk, Label, Entry, Button, messagebox
from win10toast import ToastNotifier
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw

CONFIG_FILE = "battery_config.json"

def create_config():
    """Creates default configuration if not exists."""
    if not os.path.exists(CONFIG_FILE):
        config = {
            "threshold": 75,
            "check_interval": 60
        }
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f)

def load_config():
    """Loads the configuration from the file."""
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(threshold, interval):
    """Saves the updated threshold and interval to the config file."""
    config = {"threshold": threshold, "check_interval": interval}
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

def battery_monitor(toast):
    """Monitors battery percentage and sends notifications."""
    while True:
        config = load_config()
        threshold = config["threshold"]
        interval = config["check_interval"]

        battery = psutil.sensors_battery()
        percent = battery.percent
        plugged = battery.power_plugged

        print(f"Checking battery: {percent}% plugged in: {plugged}")  # Add logging here

        if percent >= threshold and plugged:
            print(f"Battery at {percent}%. Notification triggered.")
            toast.show_toast(
                "Battery Full Alert",
                f"Battery is at {percent}%. Please unplug your charger.",
                duration=10,
                threaded=True
            )
            time.sleep(interval)  # Avoid spamming notifications
        else:
            print(f"Battery at {percent}%. No notification.")

        time.sleep(5)


def create_image():
    """Creates an icon for the system tray."""
    width = 64
    height = 64
    image = Image.new("RGBA", (width, height), (255, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, height), fill="blue")
    return image

def on_exit(icon, item):
    """Closes the application."""
    icon.stop()

def open_gui():
    """Opens a GUI window to modify settings."""
    def save_settings():
        try:
            new_threshold = int(threshold_entry.get())
            new_interval = int(interval_entry.get())
            if new_threshold < 0 or new_threshold > 100:
                raise ValueError("Threshold must be between 0 and 100.")
            if new_interval <= 0:
                raise ValueError("Interval must be greater than 0.")
            save_config(new_threshold, new_interval)
            messagebox.showinfo("Success", "Settings updated successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    config = load_config()

    gui = Tk()
    gui.title("Battery Monitor Settings")

    Label(gui, text="Battery Threshold (%)").grid(row=0, column=0, padx=10, pady=10)
    threshold_entry = Entry(gui)
    threshold_entry.insert(0, config["threshold"])
    threshold_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(gui, text="Check Interval (seconds)").grid(row=1, column=0, padx=10, pady=10)
    interval_entry = Entry(gui)
    interval_entry.insert(0, config["check_interval"])
    interval_entry.grid(row=1, column=1, padx=10, pady=10)

    Button(gui, text="Save", command=save_settings).grid(row=2, column=0, columnspan=2, pady=10)
    gui.mainloop()

def main():
    create_config()
    toast = ToastNotifier()

    Thread(target=battery_monitor, args=(toast,), daemon=True).start()

    menu = Menu(
        MenuItem("Settings", lambda icon, item: open_gui()),
        MenuItem("Exit", on_exit)
    )
    icon = Icon("Battery Monitor", create_image(), "Battery Monitor", menu)
    icon.run()

if __name__ == "__main__":
    main()
