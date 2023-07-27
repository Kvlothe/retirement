import tkinter as tk


def update_inputs(wb, ws, username):
    house_pay = house_payment_entry.get()
    insurance = insurance_entry.get()
    gas = gas_entry.get()
    car_pay = car_payment_entry.get()
    utilities = utilities_entry.get()
    food = food_household_entry.get()
    entertainment = entertainment_entry.get()
    travel = travel_entry.get()
    misc = misc_unplanned_entry.get()
    hobbies = hobbies_entry.get()
    charity = charity_entry.get()

    ws['C28'] = house_pay
    ws['C29'] = insurance
    ws['C30'] = gas
    ws['C31'] = car_pay
    ws['C32'] = utilities
    ws['C33'] = food
    ws['C34'] = entertainment
    ws['C35'] = travel
    ws['C36'] = misc
    ws['C37'] = hobbies
    ws['C38'] = charity

    wb.save(f'{username}.xlsx')


def inputs_window(input_window, wb, ws, username):
    global house_payment_entry, insurance_entry, gas_entry, car_payment_entry, utilities_entry, food_household_entry, entertainment_entry, travel_entry, misc_unplanned_entry, hobbies_entry, charity_entry

    input_window.geometry("400x600")

    # Create Label and Entry for Expense estimates
    house_payment_label = tk.Label(input_window, text="House Payment")
    house_payment_label.pack()
    house_payment_entry = tk.Entry(input_window)
    house_payment_entry.pack()
    insurance_label = tk.Label(input_window, text="Insurance, Car, ETC")
    insurance_label.pack()
    insurance_entry = tk.Entry(input_window)
    insurance_entry.pack()
    gas_label = tk.Label(input_window, text="Gas")
    gas_label.pack()
    gas_entry = tk.Entry(input_window)
    gas_entry.pack()
    car_payment_label = tk.Label(input_window, text="Car Payment")
    car_payment_label.pack()
    car_payment_entry = tk.Entry(input_window)
    car_payment_entry.pack()
    utilities_label = tk.Label(input_window, text="Utilities (Water, Electric, Phone, Internet)")
    utilities_label.pack()
    utilities_entry = tk.Entry(input_window)
    utilities_entry.pack()
    food_household_label = tk.Label(input_window, text="Food and Household")
    food_household_label.pack()
    food_household_entry = tk.Entry(input_window)
    food_household_entry.pack()
    entertainment_label = tk.Label(input_window, text="Entertainment and Eating Out")
    entertainment_label.pack()
    entertainment_entry = tk.Entry(input_window)
    entertainment_entry.pack()
    travel_label = tk.Label(input_window, text="Travel")
    travel_label.pack()
    travel_entry = tk.Entry(input_window)
    travel_entry.pack()
    misc_unplanned_label = tk.Label(input_window, text="Miscellaneous and Unplanned")
    misc_unplanned_label.pack()
    misc_unplanned_entry = tk.Entry(input_window)
    misc_unplanned_entry.pack()
    hobbies_label = tk.Label(input_window, text="Hobbies")
    hobbies_label.pack()
    hobbies_entry = tk.Entry(input_window)
    hobbies_entry.pack()
    charity_label = tk.Label(input_window, text="Charity")
    charity_label.pack()
    charity_entry = tk.Entry(input_window)
    charity_entry.pack()

    submit_basic = tk.Button(input_window, text="Submit", command=lambda: update_inputs(wb, ws, username))
    submit_basic.pack()

    input_window.mainloop()
