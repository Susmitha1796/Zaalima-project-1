# 🧾 Invoice PDF Extractor with Email Integration & GUI

This project is a Python-based desktop application that **automatically reads invoice PDFs**, extracts key fields like invoice number, date, and customer name using **regex**, and stores the data in a CSV file. It also includes:

✅ Email fetching (IMAP)  
✅ PDF reading  
✅ Regex-based text extraction  
✅ Tkinter-based GUI  
✅ Logging  
✅ Export to CSV

## 🚀 Features

- 🔍 Automatically scans your Gmail inbox for PDF invoice attachments
- 📥 Saves and processes PDFs from the attachments folder
- 📄 Extracts fields like `Invoice Number`, `Bill To`, `Date`
- 📊 Displays data in a GUI table
- 📤 Exports extracted data to `extracted_data.csv`

## 🛠️ Tech Stack

- Python 3.13+
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- Tkinter (GUI)
- Pandas
- re (Regex)
- imaplib & email (Gmail access)
- Logging module


## 🖥️ How to Run

1. 📁 Clone or download the project
2. 📍 Open terminal in this folder:  
   `C:\Users\SUSMITHA MANKU\Desktop\Zaalima\Zaalima`
3. 🐍 Run the app:
python ui.py

## 🔐 Gmail 2-Step Verification Note

If you use Gmail:

* Enable **IMAP** from Gmail Settings
* Enable **2-step verification**
* Generate an **App Password** from [Google App Passwords](https://myaccount.google.com/apppasswords)
* Use that in the app instead of your real password

## 📁 Project Structure

Zaalima/
├── attachments/
│   └── dummyinvoice.pdf
├── extracted_data.csv
├── ui.py
├── regex.py
├── email_read.py
├── invoice_app.log
└── ...

## 📦 Output Example

Invoice,Bill To,Date
INV-1001,John Doe,2025-06-18
## 🧠 Future Improvements

* Export to SQLite or Excel
* Email filters for specific senders
* AI-based OCR for scanned PDFs
## 🤝 Author

**Susmitha Manku**
Python | Automation | GUI Projects
GitHub: [Susmitha1796](https://github.com/Susmitha1796)
