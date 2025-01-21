import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from db import *
from qr_code import create_qr_code, add_data_to_qr, scan_qr_code

def exit_app():
    root.destroy()

# Main GUI setup
root = tk.Tk()
root.title("QR Code Utility")
root.geometry("400x300")

# Initialize the database
init_db()


btn_create = tk.Button(root, text="1. Create QR Code", command=create_qr_code)
btn_create.pack(pady=10)

btn_add_data = tk.Button(root, text="2. Add Data to QR Code", command=add_data_to_qr)
btn_add_data.pack(pady=10)

btn_scan = tk.Button(root, text="3. Scan QR Code", command=scan_qr_code)
btn_scan.pack(pady=10)

btn_exit = tk.Button(root, text="4. Exit", command=exit_app)
btn_exit.pack(pady=10)

# Run the app
root.mainloop()