import tkinter as tk


def update_one_time_info(wb, ws, username):
    move = move_entry.get()
    retirement_party = retirement_party_entry.get()
    initial_big_trip = initial_big_trip_entry.get()
    home_improvement = home_improvement_entry.get()
    gifts = gifts_entry.get()
    car_motor_home = car_motor_home_entry.get()
    annuity = annuity_entry.get()
    tax = tax_for_what_we_use_here_entry.get()
    misc = miscellaneous_entry.get()

    ws['K28'] = move
    ws['K29'] = retirement_party
    ws['K30'] = initial_big_trip
    ws['K31'] = home_improvement
    ws['K32'] = gifts
    ws['K33'] = car_motor_home
    ws['K34'] = annuity
    ws['K35'] = tax
    ws['K36'] = misc

    wb.save(f'{username}.xlsx')


def one_time_window(one_time_expense_window, wb, ws, username):
    global move_entry, retirement_party_entry, initial_big_trip_entry, home_improvement_entry, gifts_entry, car_motor_home_entry, annuity_entry, tax_for_what_we_use_here_entry, miscellaneous_entry

    # one_time_expense_window = tk.Tk()
    one_time_expense_window.geometry("400x400")

    # Create Labels and Entries for One Time Expense
    move_label = tk.Label(one_time_expense_window, text="Move???")
    move_label.pack()
    move_entry = tk.Entry(one_time_expense_window)
    move_entry.pack()
    retirement_party_label = tk.Label(one_time_expense_window, text="Retirement Party")
    retirement_party_label.pack()
    retirement_party_entry = tk.Entry(one_time_expense_window)
    retirement_party_entry.pack()
    initial_big_trip_label = tk.Label(one_time_expense_window, text="Initial Big Trip")
    initial_big_trip_label.pack()
    initial_big_trip_entry = tk.Entry(one_time_expense_window)
    initial_big_trip_entry.pack()
    home_improvement_label = tk.Label(one_time_expense_window, text="Home Improvement")
    home_improvement_label.pack()
    home_improvement_entry = tk.Entry(one_time_expense_window)
    home_improvement_entry.pack()
    gifts_label = tk.Label(one_time_expense_window, text="Gifts")
    gifts_label.pack()
    gifts_entry = tk.Entry(one_time_expense_window)
    gifts_entry.pack()
    car_motor_home_label = tk.Label(one_time_expense_window, text="Car or Motor home")
    car_motor_home_label.pack()
    car_motor_home_entry = tk.Entry(one_time_expense_window)
    car_motor_home_entry.pack()
    annuity_label = tk.Label(one_time_expense_window, text="Annuity**", bg="red")
    annuity_label.pack()
    annuity_entry = tk.Entry(one_time_expense_window)
    annuity_entry.pack()
    tax_for_what_we_use_here_label = tk.Label(one_time_expense_window, text="Tax for what we use here", bg="red")
    tax_for_what_we_use_here_label.pack()
    tax_for_what_we_use_here_entry = tk.Entry(one_time_expense_window)
    tax_for_what_we_use_here_entry.pack()
    miscellaneous_label = tk.Label(one_time_expense_window, text="Miscellaneous")
    miscellaneous_label.pack()
    miscellaneous_entry = tk.Entry(one_time_expense_window)
    miscellaneous_entry.pack()

    submit_basic = tk.Button(one_time_expense_window, text="Submit", command=lambda: update_one_time_info(wb, ws, username))
    submit_basic.pack()

    one_time_expense_window.mainloop()
