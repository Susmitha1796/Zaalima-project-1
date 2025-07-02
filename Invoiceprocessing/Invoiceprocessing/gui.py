
import tkinter as tk
from tkinter import filedialog, messagebox
from invoice_reader import extract_text_from_pdf
from extractor import extract_invoice_data
from database import save_to_excel, save_to_sqlite

def upload_invoice():
    path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if path:
        text = extract_text_from_pdf(path)
        data = extract_invoice_data(text)
        if data:
            save_to_excel([data], "output/gui_uploaded_invoices.xlsx")
            save_to_sqlite([data], "invoice_data.db")
            messagebox.showinfo("Success", "Invoice processed successfully!")
        else:
            messagebox.showwarning("Failed", "Could not extract invoice data.")

def run_gui():
    window = tk.Tk()
    window.title("Invoice Uploader")
    window.geometry("300x200")

    label = tk.Label(window, text="Upload and Process Invoice", font=("Arial", 14))
    label.pack(pady=20)

    upload_button = tk.Button(window, text="Upload PDF Invoice", command=upload_invoice)
    upload_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    run_gui()
