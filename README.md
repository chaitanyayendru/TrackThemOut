# 🔋 TrackThemOut - Battery Monitor Application

## 📝 Description
The **Battery Monitor Application** is a lightweight and optimized Windows desktop app that keeps track of your battery status. It alerts you when the battery charge exceeds a specified threshold, helping you extend battery life and prevent overcharging. The app runs seamlessly in the background and can be accessed via the system tray.

---

## ✨ Features
- 🖥️ **System Tray Integration**  
  - Control the app with ease through the tray menu.  

- ⚙️ **Customizable Settings**  
  - Set your preferred battery threshold and check interval through a user-friendly GUI.  

- 💻 **Low Resource Usage**  
  - Designed for efficiency, the app runs in the background with minimal impact on system performance.  

- 📢 **Native Notifications**  
  - Receive Windows notifications when the battery reaches your defined threshold.  

---

## 🚀 Installation

### Prerequisites:
- Python 3.7 or later installed on your system.
- Dependencies listed in `requirements.txt`.

### Steps:
1. Clone this repository or download the source code.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```

---

## ⚡ Configuration
- A configuration file (`battery_config.json`) stores the default settings:
  - **Threshold:** 95%
  - **Check Interval:** 60 seconds
- Modify these settings via the **Settings** option in the app’s system tray menu or the GUI.

---

## 📦 Packaging to .exe
Want to run the app without Python installed? Convert it into an executable:

1. Install **pyinstaller**:
   ```bash
   pip install pyinstaller
   ```
2. Create the `.exe`:
   ```bash
   python -m PyInstaller --onefile --noconsole app.py
   ```
3. The executable will be located in the `dist` folder.

---

## 🖼️ Icons and Appearance
The app uses a **simple blue rectangle** for the system tray icon. You can customize this icon in the code by replacing the `create_image` function.  
For notifications, the app uses Windows’ native **toast notifications**.

---

## 📚 License
This project is licensed under the MIT License. Feel free to use and modify it.

---