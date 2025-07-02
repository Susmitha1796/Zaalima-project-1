
import re

def extract_invoice_data(text):
    invoice_number = re.search(r"Invoice\s*Number[:\-]?\s*(\w+)", text, re.IGNORECASE)
    date = re.search(r"Date[:\-]?\s*([0-9]{2}/[0-9]{2}/[0-9]{4})", text)
    vendor = re.search(r"Vendor[:\-]?\s*(.+?)\n", text)
    amount = re.search(r"Total[:\-]?\s*\$?([0-9,.]+)", text)

    if invoice_number and date and amount:
        return {
            'Invoice Number': invoice_number.group(1),
            'Date': date.group(1),
            'Vendor': vendor.group(1).strip() if vendor else 'Unknown',
            'Amount': amount.group(1).replace(',', '')
        }
    return None
