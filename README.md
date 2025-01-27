

# QR Code Utility Application

## Overview

This project is a Python-based application for creating, scanning, and managing QR codes. It allows users to generate unique QR codes, add data to existing QR codes, and scan QR codes to retrieve stored information. The app uses `tkinter` for the graphical user interface and `MySQL` for storing QR code data.

## Features

- **Create QR Code**: Generate a unique QR code with a randomly generated ID.
- **Add Data to QR Code**: Add user information such as name, age, and mobile number to the QR code data stored in the database.
- **Scan QR Code**: Scan a QR code using the camera and fetch the associated data from the database.
- **Database Integration**: All QR code data is stored and managed in a MySQL database.

---

## Project Structure

- **`desktop.py`**: Main entry point for the application, containing the GUI logic.
- **`qrcode.py`**: Handles QR code generation, scanning, and processing.
- **`setup_db.py`**: Contains database initialization and functions to handle CRUD operations.
- **`__init__.py`**: Module-level initialization for both `qrcode` and `setup_db`.
- **MySQL Database**: Stores data associated with QR codes.

---

## Installation

### Prerequisites

1. Python 3.7 or higher.
2. MySQL server installed and running on your local machine.
3. Required Python packages:
   - `mysql-connector-python`
   - `qrcode`
   - `opencv-python`

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/qr-code-utility.git
   cd qr-code-utility
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the MySQL database:
   - Open MySQL Workbench or any MySQL client.
   - Create a new database named `qrcode_db`.
   - Ensure the MySQL user credentials (`root` and password `6395`) match the values in `setup_db.py`.

4. Initialize the database:
   - The database is automatically initialized when you run the application. If needed, ensure the `init_db` function is called.

---

## Usage

1. Run the application:
   ```bash
   python desktop.py
   ```

2. Interact with the GUI:
   - **Create QR Code**: Click "Create QR Code" to generate a new QR code.
   - **Add Data to QR Code**: Click "Add Data to QR Code" and provide the required information.
   - **Scan QR Code**: Click "Scan QR Code" to scan a QR code using the camera and fetch data.

---

## Folder Structure

```
qr-code-utility/
├── desktop.py         # Main GUI application
├── qrcode.py          # QR code generation and scanning logic
├── setup_db.py        # Database setup and operations
├── __init__.py        # Module initialization
├── requirements.txt   # List of dependencies
├── README.md          # Project documentation
├── generated-qrcode/  # Folder to store generated QR codes
```

---

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and create a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contact

For any queries, feel free to contact:
- **Name**: Reesu Shrivastava  
- **Email**: reesushrivastava@gmail.com  

Happy coding! 🎉