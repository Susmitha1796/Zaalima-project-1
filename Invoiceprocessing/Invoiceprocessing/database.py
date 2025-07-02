
import pandas as pd
import sqlite3
import os

def save_to_excel(data, filepath):
    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_excel(filepath, index=False)
    print(f"Saved to Excel: {filepath}")

def save_to_sqlite(data, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS invoices (
            invoice_number TEXT PRIMARY KEY,
            date TEXT,
            vendor TEXT,
            amount REAL
        )
    """)
    for item in data:
        try:
            cursor.execute("""
                INSERT INTO invoices (invoice_number, date, vendor, amount)
                VALUES (?, ?, ?, ?)
            """, (item['Invoice Number'], item['Date'], item['Vendor'], float(item['Amount'])))
        except sqlite3.IntegrityError:
            print(f"Duplicate invoice: {item['Invoice Number']}")
    conn.commit()
    conn.close()
    print(f"Saved to SQLite DB: {db_path}")
