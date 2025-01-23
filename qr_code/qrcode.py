import qrcode
import cv2
import random
from datetime import datetime
import string
from db import init_db, save_to_db, fetch_from_db , update_to_db
import tkinter as tk
from tkinter import messagebox, filedialog

# Initialize the database
init_db()

def getRandomId():
    let = ''.join(random.choices(string.ascii_letters, k=5))
    cdt = datetime.now().strftime('%y%m%d%H%M%S')
    let1 = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    return let + cdt + let1

def create_qr_code():
    unique_id = getRandomId()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(unique_id)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img.save(f"generated-qrcode/{unique_id}.png")
    save_to_db(unique_id)
    messagebox.showinfo("Success", f"QR Code created with ID: {unique_id} and saved to the database!")

def process_camera():
        cap = cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()

        while True:
            ret, frame = cap.read()
            if not ret:
                messagebox.showerror("Error", "Failed to access the camera.")
                break

            data, bbox, _ = detector.detectAndDecode(frame)
            if data:
                cap.release()
                cv2.destroyAllWindows()
                return data

            cv2.imshow("QR Code Scanner", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

def scan_qr_code():
    process_qr_data(process_camera())

def process_qr_data(data):
    result = fetch_from_db(data)
    if result:
        messagebox.showinfo("QR Code Data", f"Data Found in Database:\n\nID: {result[1]}\nName: {result[2]}\nAge: {result[3]}\nMobile: {result[4]}")
    else:
        messagebox.showerror("Error", "QR Code not found in the database.")

def add_data_to_qr():
    existing_data = process_camera()
    print(existing_data,"in add to qr ")
    def on_submit():
        name = name_entry.get()
        age = age_entry.get()
        mob_no = mob_entry.get()

        print("id, name, age, mob_no", existing_data, name, age, mob_no)        

        if not name or not age or not mob_no:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            age = int(age)
            mob_no = int(mob_no)
        except ValueError:
            messagebox.showerror("Error", "Age and Mobile Number must be numeric!")
            return

        if existing_data:
            try:
                update_to_db(existing_data, name, age, mob_no)
                messagebox.showinfo("Success", "Data added to the database successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save data to the database: {e}")
        else:
            messagebox.showerror("Error", "No unique ID provided to add data.")
            return

        root.destroy()


    root = tk.Tk()
    root.title("Add Data to QR Code")

    tk.Label(root, text="Enter Your Details").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(root, text="Name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    name_entry = tk.Entry(root)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Age:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    age_entry = tk.Entry(root)
    age_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Mobile Number:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    mob_entry = tk.Entry(root)
    mob_entry.grid(row=3, column=1, padx=10, pady=5)

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()
