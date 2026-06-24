import tkinter as tk
from tkinter import scrolledtext

monitoring = False


def start_monitoring():
    global monitoring
    monitoring = True
    status_label.config(text="Status: Monitoring")
    log_box.insert(tk.END, "Monitoring started\n")
    log_box.see(tk.END)


def stop_monitoring():
    global monitoring
    monitoring = False
    status_label.config(text="Status: Stopped")
    log_box.insert(tk.END, "Monitoring stopped\n")
    log_box.see(tk.END)


# Create main window
root = tk.Tk()
root.title("WiFiGuard")
root.geometry("600x400")

# Title
title = tk.Label(
    root,
    text="WiFiGuard",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

# Trusted Network Label
network_label = tk.Label(
    root,
    text="Trusted Network: realme P1 Pro 5G",
    font=("Arial", 11)
)
network_label.pack()

# Status Label
status_label = tk.Label(
    root,
    text="Status: Stopped",
    font=("Arial", 12)
)
status_label.pack(pady=10)

# Start Button
start_btn = tk.Button(
    root,
    text="Start Monitoring",
    width=20,
    command=start_monitoring
)
start_btn.pack(pady=5)

# Stop Button
stop_btn = tk.Button(
    root,
    text="Stop Monitoring",
    width=20,
    command=stop_monitoring
)
stop_btn.pack(pady=5)

# Log Box
log_box = scrolledtext.ScrolledText(
    root,
    width=70,
    height=12
)
log_box.pack(pady=15)

# Run application
root.mainloop()