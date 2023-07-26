import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
from datetime import datetime
import os
import openpyxl
import currentProfile
import basicInfo


def load_or_create_profile():
    global wb, ws, username  # declare them as global so we can access them later
    username = name_entry.get()
    filename = f'{username}.xlsx'
    if os.path.exists(filename):
        wb = openpyxl.load_workbook(filename)
        print(f"Loaded existing profile for {username}")
    else:
        wb = openpyxl.load_workbook('Sample.xlsx')
        print(f"Created new profile for {username}")
    ws = wb.active
    window.destroy()  # This will close the current window
    main_menu_window()  # This will open a new window


def main_menu_window():
    global main_window
    main_window = tk.Tk()
    main_window.geometry("400x400")
    # basic = tk.Button(main_window, text="Basic info", command=basicInfo.basic_info_window)
    basic = tk.Button(main_window, text="Basic info", command=lambda: basicInfo.basic_info_window(wb, ws, username))
    basic.pack()
    # current = tk.Button(main_window, text="Current Profile", command=currentProfile.current_profile_window)
    current = tk.Button(main_window, text="Current Profile", command=lambda: currentProfile.current_profile_window(wb, ws, username))
    current.pack()
    social_security = tk.Button(main_window, text='Social Security', command=socialSecurity.security_window)
    social_security.pack()
    pension = tk.Button(main_window, text="Pension (Monthly)", command=pension.pension_window)
    pension.pack()
    estimated_expenses = tk.Button(main_window, text="Estimated Expenses", command=estimatedExpenses.expenses_window)
    estimated_expenses.pack()


# Create a window
window = tk.Tk()
window.geometry("200x100")
# window.geometry("1280x800")

name_label = tk.Label(window, text="Name")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

load_button = tk.Button(window, text="Load or Create Profile", command=load_or_create_profile)
load_button.pack()

window.mainloop()
