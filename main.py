from datetime import datetime
import tkinter as tk
from tkinter import ttk
from openpyxl import load_workbook

# Load workbook and Select the active worksheet
wb = load_workbook('sample.xlsx')
ws = wb.active


def update_excel():
    # Retrieve the input as a string and convert it to an integer
    year_input = int(year_entry.get())
    # Place the input into the Excel worksheet
    ws['C5'] = year_input
    age_input = int(age_entry.get())
    ws['C6'] = age_input
    retirement_age_input = int(retirement_age_combo.get())
    ws['C7'] = retirement_age_input
    ss_s1_input = int(ss_s1_combo.get())
    ws['C8'] = ss_s1_input
    ss_s2_input = int(ss_s2_combo.get())
    ws['E8'] = ss_s2_input
    pension_s1_input = pension_s1_combo.get()
    if pension_s1_input == 'lump':
        ws['C9'] = pension_s1_input
    else:
        pension_s1_input = int(pension_s1_combo.get())
        ws['C9'] = pension_s1_input
    # pension_s2_input = int(pension_s2_combo.get())
    pension_s2_input = pension_s2_combo.get()
    if pension_s2_input == 'lump':
        ws['E9'] = pension_s2_input
    else:
        pension_s2_input = int(pension_s2_combo.get())
        ws['E9'] = pension_s2_input
    other_income_s1_input = int(other_income_s1_combo.get())
    ws['C10'] = other_income_s1_input
    other_income_s2_input = int(other_income_s2_combo.get())
    ws['E10'] = other_income_s2_input
    pre_tax_input = int(pre_tax_entry.get())
    ws['C13'] = pre_tax_input
    after_tax_input = int(after_tax_entry.get())
    ws['C14'] = after_tax_input
    ss_s1_full_input = int(ss_s1_entry.get())
    ws['C18'] = ss_s1_full_input
    ss_s2_full_input = int(ss_s2_entry.get())
    ws['C19'] = ss_s2_full_input
    pension_s1_monthly_input = int(pension_s1_entry.get())
    ws['C22'] = pension_s1_monthly_input
    pension_s2_monthly_input = int(pension_s2_entry.get())
    ws['D22'] = pension_s2_monthly_input
    cell_e22_input = int(cell_e22.get())
    ws['E22'] = cell_e22_input
    cell_c23_input = int(cell_c23.get())
    ws['C23'] = cell_c23_input
    cell_d23_input = int(cell_d23.get())
    ws['D23'] = cell_d23_input
    cell_e23_input = int(cell_e23.get())
    ws['E23'] = cell_e23_input
    cell_c28_input = int(cell_c28.get())
    ws['C28'] = cell_c28_input
    cell_c29_input = int(cell_c29.get())
    ws['C29'] = cell_c29_input
    cell_c30_input = int(cell_c30.get())
    ws['C30'] = cell_c30_input
    cell_c31_input = int(cell_c31.get())
    ws['C31'] = cell_c31_input
    cell_c32_input = int(cell_c32.get())
    ws['C32'] = cell_c32_input
    cell_c33_input = int(cell_c33.get())
    ws['C33'] = cell_c33_input
    cell_c34_input = int(cell_c34.get())
    ws['C34'] = cell_c34_input
    cell_c35_input = int(cell_c35.get())
    ws['C35'] = cell_c35_input
    cell_c36_input = int(cell_c36.get())
    ws['C36'] = cell_c36_input
    cell_c37_input = int(cell_c37.get())
    ws['C37'] = cell_c37_input
    cell_c38_input = int(cell_c38.get())
    ws['C38'] = cell_c38_input

    # cell_c_input = int(cell_c.get())
    # ws['C'] = cell_c_input

    wb.save('sample.xlsx')


# def combo_selection(event):
#     # Get the combo box selection
#     selected = retirement_age_combo.get()
#     print(f'Selected item: {selected}')


# Create a window
window = tk.Tk()
window.geometry("1280x800")

basic_info_label = tk.Label(window, text="Basic Information", bg="Blue")
current_profile_label = tk.Label(window, text="Current Portfolio", bg="Blue")
social_security_label = tk.Label(window, text="Social Security at Full Retirement (67)", bg="Blue")
pension_label = tk.Label(window, text="Pension (monthly) (100% survivor)", bg="Blue")
expense_estimate_label = tk.Label(window, text="Expense Estimate", bg="Blue")
one_time_expense_label = tk.Label(window, text="One Time Expenses", bg="Blue")
medical_label = tk.Label(window, text="Medical", bg="Blue")
other_assumptions_label = tk.Label(window, text="Other Expenses and Assumptions", bg="Blue")
growth_investment_label = tk.Label(window, text="Growth and Investment Assumptions", bg="Blue")

# Create a Label and an Entry for Current Year
year_label = tk.Label(window, text="Current Year:")
year_entry = tk.Entry(window)

# Create a Label and Entry for Age
age_label = tk.Label(window, text="Enter Your age")
age_entry = tk.Entry(window)

# Create a Combobox for Retirement age
age_to_retire = tk.Label(window, text="Retirement Age")
retirement_age_combo = ttk.Combobox(window, values=["62", "65", "67", "70"])
# retirement_age_combo.bind('<<ComboboxSelected>>', combo_selection)

year_take_ss_label = tk.Label(window, text="Age to Take Social Security")
# Create a Combobox for SS
year_ss_s1 = tk.Label(window, text="Self")
ss_s1_combo = ttk.Combobox(window, values=["62", "65", "67", "70"])

# Create a Combobox for SS Spouse
year_ss_s2 = tk.Label(window, text="Spouse")
ss_s2_combo = ttk.Combobox(window, values=["62", "65", "67", "70"])

year_take_pension_label = tk.Label(window, text="Age to take Pension")
# Create a Combobox for pension
pension_s1 = tk.Label(window, text="Self")
pension_s1_combo = ttk.Combobox(window, values=["62", "65", "lump"])

# Create a Combobox for pension for spouse
pension_s2 = tk.Label(window, text="Spouse")
pension_s2_combo = ttk.Combobox(window, values=["62", "65", "lump"])

year_other_income_label = tk.Label(window, text="Year to take Other Income  (Annuity, ETC)")
# Create a Combobox for other incomes
other_income_s1 = tk.Label(window, text="Self")
other_income_s1_combo = ttk.Combobox(window, values=["62", "65", "67", "70"])
other_income_s2 = tk.Label(window, text="Spouse")
other_income_s2_combo = ttk.Combobox(window, values=["62", "65", "67", "70"])

# Create Label and Entry for Current Portfolio
pre_tax_label = tk.Label(window, text="Pre Tax - (IRA, 401K, 403B, HSA)")
pre_tax_entry = tk.Entry(window)
after_tax_label = tk.Label(window, text="After Tax - (Stock, Cash, Savings)")
after_tax_entry = tk.Entry(window)

# Create Label and Entry for Social Security
ss_s1_label = tk.Label(window, text="Self")
ss_s1_entry = tk.Entry(window)
ss_s2_label = tk.Label(window, text="Spouse")
ss_s2_entry = tk.Entry(window)

# Create Label and Entry for Pensions
pension_63_label = tk.Label(window, text="63")
pension_65_label = tk.Label(window, text="65")
pension_lump_label = tk.Label(window, text="Lump")
pension_self_label = tk.Label(window, text="Self")
pension_s1_63_entry = tk.Entry(window)
pension_s1_65_entry = tk.Entry(window)
pension_s1_lump_entry = tk.Entry(window)
pension_spouse_label = tk.Label(window, text="Spouse")
pension_s2_63_entry = tk.Entry(window)
pension_s2_65_entry = tk.Entry(window)
pension_s2_lump_entry = tk.Entry(window)

# Create Label and Entry for Expense estimates
house_payment_label = tk.Label(window, text="House Payment")
house_payment_entry = tk.Entry(window)
insurance_label = tk.Label(window, text="Insurance, Car, ETC")
insurance_entry = tk.Entry(window)
gas_label = tk.Label(window, text="Gas")
gas_entry = tk.Entry(window)
car_payment_label = tk.Label(window, text="Car Payment")
car_payment_entry = tk.Entry(window)
utilities_label = tk.Label(window, text="Utilities (Water, Electric, Phone, Internet)")
utilities_entry = tk.Entry(window)
food_household_label = tk.Label(window, text="Food and Household")
food_household_entry = tk.Entry(window)
entertainment_label = tk.Label(window, text="Entertainment and Eating Out")
entertainment_entry = tk.Entry(window)
travel_label = tk.Label(window, text="Travel")
travel_entry = tk.Entry(window)
misc_unplanned_label = tk.Label(window, text="Miscellaneous and Unplanned")
misc_unplanned_entry = tk.Entry(window)
hobbies_label = tk.Label(window, text="Hobbies")
hobbies_entry = tk.Entry(window)
charity_label = tk.Label(window, text="Charity")
charity_entry = tk.Entry(window)

# Create Label and Entry for Medical
medical_expense_label = tk.Label(window, text="Medical")
medical_expense_entry = tk.Entry(window)

# Create Labels and Entries for One Time Expense
move_label = tk.Label(window, text="Move???")
move_entry = tk.Entry(window)
retirement_party_label = tk.Label(window, text="Retirement Party")
retirement_party_entry = tk.Entry(window)
initial_big_trip_label = tk.Label(window, text="Initial Big Trip")
initial_big_trip_entry = tk.Entry(window)
home_improvement_label = tk.Label(window, text="Home Improvement")
home_improvement_entry = tk.Entry(window)
gifts_label = tk.Label(window, text="Gifts")
gifts_entry = tk.Entry(window)
car_motor_home_label = tk.Label(window, text="Car or Motor home")
car_motor_home_entry = tk.Entry(window)
annuity_label = tk.Label(window, text="Annuity**", bg="red")
annuity_entry = tk.Entry(window)
tax_for_what_we_use_here_label = tk.Label(window, text="Tax for what we use here", bg="red")
tax_for_what_we_use_here_entry = tk.Entry(window)
miscellaneous_label = tk.Label(window, text="Miscellaneous")
miscellaneous_entry = tk.Entry(window)

# Pack the widgets
basic_info_label.place(x=0, y=0)
year_label.place(x=10, y=20)
year_entry.place(x=100, y=20)
age_label.place(x=10, y=40)
age_entry.place(x=100, y=40)
age_to_retire.place(x=10, y=60)
retirement_age_combo.place(x=100, y=60)

year_take_ss_label.place(x=0, y=90)
year_ss_s1.place(x=10, y=110)
ss_s1_combo.place(x=100, y=110)
year_ss_s2.place(x=10, y=130)
ss_s2_combo.place(x=100, y=130)

year_take_pension_label.place(x=0, y=155)
pension_s1.place(x=10, y=175)
pension_s1_combo.place(x=100, y=175)
pension_s2.place(x=10, y=195)
pension_s2_combo.place(x=100, y=195)

year_other_income_label.place(x=0, y=220)
other_income_s1.place(x=10, y=240)
other_income_s1_combo.place(x=100, y=240)
other_income_s2.place(x=10, y=260)
other_income_s2_combo.place(x=100, y=260)

current_profile_label.place(x=0, y=300)
pre_tax_label.place(x=10, y=320)
pre_tax_entry.place(x=100, y=340)
after_tax_label.place(x=10, y=360)
after_tax_entry.place(x=100, y=380)

social_security_label.place(x=0, y=400)
ss_s1_label.place(x=10, y=420)
ss_s1_entry.place(x=100, y=420)
ss_s2_label.place(x=10, y=440)
ss_s2_entry.place(x=100, y=440)

pension_label.place(x=0, y=480)
pension_self_label.place(x=10, y=500)
pension_s1_63_entry.place(x=100, y=500)
pension_spouse_label.place(x=10, y=520)
pension_s2_63_entry.place(x=100, y=520)

# Work on column 2 Estimated expenses and one time expenses
expense_estimate_label.place(x=280, y=0)
house_payment_label.place(x=300, y=20)
house_payment_entry.place(x=420, y=20)
insurance_label.place(x=300, y=40)
insurance_entry.place(x=420, y=40)
gas_label.place(x=300, y=60)
gas_entry.place(x=420, y=60)
car_payment_label.place(x=300, y=80)
car_payment_entry.place(x=420, y=80)
hobbies_label.place(x=300, y=100)
hobbies_entry.place(x=420, y=100)
charity_label.place(x=300, y=120)
charity_entry.place(x=420, y=120)
food_household_label.place(x=300, y=140)
food_household_entry.place(x=420, y=140)
travel_label.place(x=300, y=160)
travel_entry.place(x=420, y=160)
misc_unplanned_label.place(x=300, y=180)
misc_unplanned_entry.place(x=420, y=200)
entertainment_label.place(x=300, y=220)
entertainment_entry.place(x=420, y=240)
utilities_label.place(x=300, y=260)
utilities_entry.place(x=420, y=280)
# Medical
medical_label.place(x=280, y=320)
# medical_expense_label.place(x=300, y=320)
medical_expense_entry.place(x=420, y=320)
# One Time
one_time_expense_label.place(x=280, y=400)
move_label.place(x=300, y=420)
move_entry.place(x=420, y=420)
retirement_party_label.place(x=300, y=440)
retirement_party_entry.place(x=420, y=440)
initial_big_trip_label.place(x=300, y=460)
initial_big_trip_entry.place(x=420, y=460)
home_improvement_label.place(x=300, y=480)
home_improvement_entry.place(x=420, y=480)
gifts_label.place(x=300, y=500)
gifts_entry.place(x=420, y=500)
car_motor_home_label.place(x=300, y=520)
car_motor_home_entry.place(x=420, y=520)
# Ask Dad, marked in RED
annuity_label.place(x=300, y=560)
annuity_entry.place(x=420, y=560)
tax_for_what_we_use_here_label.place(x=300, y=580)
tax_for_what_we_use_here_entry.place(x=420, y=600)


# other_assumptions_label.pack()

# growth_investment_label.pack()

# Create a Submit button to save to xlsx
# submit_button = tk.Button(window, text="Submit", command=update_excel)
# submit_button.pack()

# Populate the Entry field with the current year
current_year = datetime.now().year
year_entry.insert(0, str(current_year))

# Create a button that triggers the update_excel function when clicked
# submit_button = tk.Button(window, text="Submit", command=update_excel)
# submit_button.grid(row=30, column=4)

# Run the main event loop
window.mainloop()
