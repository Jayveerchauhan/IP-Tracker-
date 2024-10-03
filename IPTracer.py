"""
Created on Sat Jun  8 23:30:47 2024

@author: Aniket Rai
"""

import tkinter as tk
from tkinter import filedialog, messagebox, Label
from PIL import Image, ImageTk
import csv
import IP2Location
import ipaddress
import os
import sys


if hasattr(sys, '_MEIPASS'):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")


#database = IP2Location.IP2Location(db_path)


def get_ip_details(ip, db):
    try:
        rec = db.get_all(ip)
        details = {
            "country": rec.country_long,
            "region": rec.region,
            "city": rec.city,
            "latitude": rec.latitude,
            "longitude": rec.longitude,
            "zip_code": rec.zipcode,
            "time_zone": rec.timezone
        }
        return details
    except Exception as e:
        print(f"Error fetching details for {ip}: {e}")
        return None

def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def p_file(input_filename, output_filename, db):
    ips = []
    with open(input_filename, 'r', encoding='utf-8') as file:
        for line in file:
            ip = line.strip()
            if ip and check_ip(ip):
                ips.append(ip)

    results = []
    for ip in ips:
        details = get_ip_details(ip, db)
        if details:
            results.append({"ip": ip, "details": details})
        else:
            results.append({"ip": ip, "details": "Not found"})

    with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["ip", "details"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for data in results:
            writer.writerow(data)

def o_file():
    filename = filedialog.askopenfilename(
        title="Select IP Address File",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    if filename:
        return filename
    return None

def s_file():
    filename = filedialog.asksaveasfilename(
        title="Save CSV File",
        defaultextension=".csv",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )
    if filename:
        return filename
    return None

def lookup():
    input_filename = o_file()
    if not input_filename:
        return
    
    output_filename = s_file()
    if not output_filename:
        return

    database_filename = 'database.BIN'
    if not os.path.isfile(database_filename):
        messagebox.showerror("Error", f"Database file {database_filename} not found.")
        return

    db = IP2Location.IP2Location(database_filename)
    p_file(input_filename, output_filename, db)
    messagebox.showinfo("Success", f"IP details have been saved to {output_filename}")

def create_gui():
    root = tk.Tk()
    root.title("IP Tracer")
    root.geometry("600x400")
    root.resizable(0,0)
    
    img1 = Image.open("logo.png")
    img2 = ImageTk.PhotoImage(img1)

    lbl1 = Label(root,image=img2)
    lbl1.image = img2 
    lbl1.place(x=195, y=5)
    
    label1 = tk.Label(root, text="IP TRACER", font=("Arial Bold", 24))
    label1.place(x=202, y=200)

    label2 = tk.Label(root, text="By Aniket Rai", font=("Arial Bold", 10))
    label2.place(x=500, y=377)


    button = tk.Button(root, text="Lookup IPs", command=lookup, background = 'aqua', foreground ="black",font=("Arial bold",14),bd=6)
    button.place(x=224, y=300)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
