import qrcode
import cv2
import random
from datetime import datetime
import string
from db import *
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from PIL import Image

def getRandomId():
    let = ''.join(random.choices(string.ascii_letters, k=5))
    cdt = datetime.now().strftime('%y%m%d%H%M%S')
    let1 = ''.join(random.choices(string.ascii_letters+string.digits, k=5))
    id = let+cdt+let1
    return id

def create_qr_code():
    data = getRandomId()
    if data:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        img.save("generated-qrcode/"+data+".png")
        # init_db()
        save_to_db(data)
        messagebox.showinfo("Success", "QR Code created successfully and data saved to database!")

def add_data_to_qr():
    qr_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if qr_path:
        img = Image.open(qr_path)
        data = simpledialog.askstring("Input", "Enter the data to add to the QR Code:")
        if data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            new_img = qr.make_image(fill_color="black", back_color="white")

            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                new_img.save(save_path)
                save_to_db(data)
                messagebox.showinfo("Success", "Data added to QR Code successfully and saved to database!")
        else:
            messagebox.showerror("Error", "No data entered to add to QR Code.")

def scan_qr_code():
    qr_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if qr_path:
        img = cv2.imread(qr_path)
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            messagebox.showinfo("QR Code Data", f"Valid QR Code!\nData: {data}")
        else:
            messagebox.showerror("Error", "Invalid QR Code or no data found.")
