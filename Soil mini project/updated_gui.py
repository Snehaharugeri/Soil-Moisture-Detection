import tkinter as tk
from tkinter import ttk
import serial
import threading
import time
import joblib
import numpy as np

def update_gui(moisture, label):
    moisture_var.set(f"Moisture: {moisture}")
    status_var.set(f"Soil Status: {label}")

def read_serial():
    while True:
        try:
            if ser.in_waiting:
                line = ser.readline().decode().strip()
                if line.isdigit():
                    moisture = int(line)
                    prediction = model.predict(np.array([[moisture]]))[0]
                    update_gui(moisture, prediction)
        except Exception as e:
            print("Error:", e)
        time.sleep(1)

def main():
    global root, moisture_var, status_var, ser, model
    model = joblib.load("moisture_classifier.pkl")
    ser = serial.Serial('COM9', 9600, timeout=1)

    root = tk.Tk()
    root.title("Soil Moisture Monitor")
    root.geometry("400x200")

    moisture_var = tk.StringVar()
    status_var = tk.StringVar()

    ttk.Label(root, text="Soil Moisture Monitoring", font=("Helvetica", 16, "bold")).pack(pady=10)
    ttk.Label(root, textvariable=moisture_var, font=("Helvetica", 14)).pack(pady=10)
    ttk.Label(root, textvariable=status_var, font=("Helvetica", 14)).pack(pady=10)

    threading.Thread(target=read_serial, daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    main()
