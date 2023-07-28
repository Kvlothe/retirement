from datetime import datetime
from tkinter import ttk
import tkinter as tk


def update_basic_info(wb, ws, username):
    # global main_window
    current_year = year_entry.get()
    age = age_entry.get()
    retirement_age = retirement_age_combo.get()
    ss_s1 = ss_s1_combo.get()
    ss_s2 = ss_s2_combo.get()
    pension_s1 = pension_s1_combo.get()
    pension_s2 = pension_s2_combo.get()
    other_income_s1 = other_income_s1_combo.get()
    other_income_s2 = other_income_s2_combo.get()

    ws['C5'] = int(current_year)
    ws['C6'] = int(age)
    ws['C7'] = int(retirement_age)
    ws['C8'] = int(ss_s1)
    ws['E8'] = int(ss_s2)
    ws['C9'] = int(pension_s1)
    ws['E9'] = int(pension_s2)
    ws['C10'] = int(other_income_s1)
    ws['E10'] = int(other_income_s2)

    wb.save(f'{username}.xlsx')


def basic_info_window(basic_window, wb, ws, username):
    global year_entry, age_entry, retirement_age_combo, ss_s1_combo, ss_s2_combo, pension_s1_combo, pension_s2_combo, other_income_s1_combo, other_income_s2_combo

    # basic_window = tk.Tk()
    basic_window.geometry("400x500")
    year_value = ws['C5'].value if ws['C5'].value else ""
    age_value = ws['C6'].value if ws['C6'].value else ""
    retirement_age_value = ws['C7'].value if ws['C7'].value else ""
    ss_s1_value = ws['C8'].value if ws['C7'].value else ""
    ss_s2_value = ws['E8'].value if ws['E8'].value else ""
    pension_s1_value = ws['C9'].value if ws['C9'].value else ""
    pension_s2_value = ws['E9'].value if ws['E9'].value else ""
    other_income_s1_value = ws['C10'].value if ws['C10'].value else ""
    other_income_s2_value = ws['E10'].value if ws['E10'].value else ""

    # Create a Label and an Entry for Current Year
    year_label = tk.Label(basic_window, text="Current Year:")
    year_label.pack()
    year_entry = tk.Entry(basic_window)
    # year_entry.insert(0, year_value)
    year_entry.pack()

    # Create a Label and Entry for Age
    age_label = tk.Label(basic_window, text="Enter Your age")
    age_label.pack()
    age_entry = tk.Entry(basic_window)
    age_entry.insert(0, age_value)
    age_entry.pack()

    # Create a Combobox for Retirement age
    age_to_retire = tk.Label(basic_window, text="Retirement Age")
    age_to_retire.pack()
    retirement_age_combo = ttk.Combobox(basic_window, values=["62", "65", "67", "70"])
    retirement_age_combo.insert(0, retirement_age_value)
    retirement_age_combo.pack()

    # Create a Combobox for SS
    year_take_ss_label = tk.Label(basic_window, text="Age to Take Social Security")
    year_take_ss_label.pack()
    year_ss_s1 = tk.Label(basic_window, text="Self")
    year_ss_s1.pack()
    ss_s1_combo = ttk.Combobox(basic_window, values=["62", "65", "67", "70"])
    ss_s1_combo.insert(0, ss_s1_value)
    ss_s1_combo.pack()

    # Create a Combobox for SS Spouse
    year_ss_s2 = tk.Label(basic_window, text="Spouse")
    year_ss_s2.pack()
    ss_s2_combo = ttk.Combobox(basic_window, values=["62", "65", "67", "70"])
    ss_s2_combo.insert(0, ss_s2_value)
    ss_s2_combo.pack()

    year_take_pension_label = tk.Label(basic_window, text="Age to take Pension")
    year_take_pension_label.pack()
    # Create a Combobox for pension
    pension_s1 = tk.Label(basic_window, text="Self")
    pension_s1.pack()
    pension_s1_combo = ttk.Combobox(basic_window, values=["62", "65", "lump"])
    pension_s1_combo.insert(0, pension_s1_value)
    pension_s1_combo.pack()

    # Create a Combobox for pension for spouse
    pension_s2 = tk.Label(basic_window, text="Spouse")
    pension_s2.pack()
    pension_s2_combo = ttk.Combobox(basic_window, values=["62", "65", "lump"])
    pension_s2_combo.insert(0, pension_s2_value)
    pension_s2_combo.pack()

    year_other_income_label = tk.Label(basic_window, text="Year to take Other Income  (Annuity, ETC)")
    year_other_income_label.pack()
    # Create a Combobox for other incomes
    other_income_s1 = tk.Label(basic_window, text="Self")
    other_income_s1.pack()
    other_income_s1_combo = ttk.Combobox(basic_window, values=["62", "65", "67", "70"])
    other_income_s1_combo.insert(0, other_income_s1_value)
    other_income_s1_combo.pack()
    other_income_s2 = tk.Label(basic_window, text="Spouse")
    other_income_s2.pack()
    other_income_s2_combo = ttk.Combobox(basic_window, values=["62", "65", "67", "70"])
    other_income_s2_combo.insert(0, other_income_s2_value)
    other_income_s2_combo.pack()

    # submit_basic = tk.Button(basic_window, text="Submit", command=update_basic_info)
    submit_basic = tk.Button(basic_window, text="Submit", command=lambda: update_basic_info(wb, ws, username))
    submit_basic.pack()

    # Populate the Entry field with the current year
    current_year = datetime.now().year
    year_entry.insert(0, str(current_year))

    basic_window.mainloop()
