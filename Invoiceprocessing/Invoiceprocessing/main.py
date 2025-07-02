from invoice_reader import read_invoices_from_folder, extract_text_from_pdf
from extractor import extract_invoice_data
from database import save_to_excel, save_to_sqlite
import os

FOLDER = "invoices"
OUTPUT_EXCEL = "output/invoices.xlsx"
DB_FILE = "invoice_data.db"

def main():
    pdf_files = read_invoices_from_folder(FOLDER)
    all_data = []

    for file_path in pdf_files:
        text = extract_text_from_pdf(file_path)
        data = extract_invoice_data(text)
        if data:
            all_data.append(data)

    
    print("Extracted Data:", all_data)

    if all_data:
        save_to_excel(all_data, OUTPUT_EXCEL)
        save_to_sqlite(all_data, DB_FILE)
        print(f"Processed {len(all_data)} invoices.")
    else:
        print("No valid invoices found.")

if __name__ == "__main__":
    main()
