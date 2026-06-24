import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import subprocess
TRUSTED_NETWORK = "realme P1 Pro 5G"

monitoring = False
def get_current_wifi():
    try:
        result = subprocess.run(
            ["netsh", "wlan", "show", "interfaces"],
            capture_output=True,
            text=True
        )

        for line in result.stdout.splitlines():
            if "SSID" in line and "BSSID" not in line:
                return line.split(":")[1].strip()

    except:
        pass

    return "Not Connected"
def add_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}"

    log_box.insert(tk.END, log_message + "\n")
    log_box.see(tk.END)

    with open("wifilog.txt", "a", encoding="utf-8") as logfile:
        logfile.write(log_message + "\n")
def update_wifi():
    wifi_name = get_current_wifi()
    wifi_label.config(text=f"Current Wi-Fi: {wifi_name}")

    if wifi_name == TRUSTED_NETWORK:
        status_network_label.config(
            text="Network Status: Trusted",
            fg="green"
        )
    elif wifi_name == "Not Connected":
        status_network_label.config(
            text="Network Status: Disconnected",
            fg="black"
        )
    else:
        status_network_label.config(
            text="Network Status: Untrusted",
            fg="red"
        )

    root.after(3000, update_wifi)
def start_monitoring():
    global monitoring
    monitoring = True
    status_label.config(text="Status: Monitoring")
    add_log("Monitoring started")

def stop_monitoring():
    global monitoring
    monitoring = False
    status_label.config(text="Status: Stopped")
    add_log("Monitoring stopped")

root = tk.Tk()
root.title("WiFiGuard")
root.geometry("700x500")

title = tk.Label(
    root,
    text="WiFiGuard",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

network_label = tk.Label(
    root,
    text=f"Trusted Network: {TRUSTED_NETWORK}",
    font=("Arial", 12)
)
network_label.pack()
wifi_label = tk.Label(
    root,
    text="Current Wi-Fi: Checking...",
    font=("Arial", 12)
)
wifi_label.pack(pady=5)
status_network_label = tk.Label(
    root,
    text="Network Status: Unknown",
    font=("Arial", 12, "bold")
)
status_network_label.pack(pady=5)
status_label = tk.Label(
    root,
    text="Status: Stopped",
    font=("Arial", 12)
)
status_label.pack(pady=10)

start_btn = tk.Button(
    root,
    text="Start Monitoring",
    width=20,
    command=start_monitoring
)
start_btn.pack(pady=5)

stop_btn = tk.Button(
    root,
    text="Stop Monitoring",
    width=20,
    command=stop_monitoring
)
stop_btn.pack(pady=5)

log_box = scrolledtext.ScrolledText(
    root,
    width=80,
    height=15
)
log_box.pack(pady=15)
update_wifi()
root.mainloop()