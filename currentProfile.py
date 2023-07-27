import tkinter as tk


def update_current_profile(wb, ws, username):
    pre_tax = pre_tax_entry.get()
    after_tax = after_tax_entry.get()
    ws['C18'] = pre_tax
    ws['C19'] = after_tax

    wb.save(f'{username}.xlsx')


def current_profile_window(current_window, wb, ws, username):
    global pre_tax_entry, after_tax_entry

    # current_window = tk.Tk()
    current_window.geometry("200x120")

    # Create Label and Entry for Current Portfolio
    pre_tax_label = tk.Label(current_window, text="Pre Tax - (IRA, 401K, 403B, HSA)")
    pre_tax_label.pack()
    pre_tax_entry = tk.Entry(current_window)
    pre_tax_entry.pack()

    after_tax_label = tk.Label(current_window, text="After Tax - (Stock, Cash, Savings)")
    after_tax_label.pack()
    after_tax_entry = tk.Entry(current_window)
    after_tax_entry.pack()

    submit_current = tk.Button(current_window, text="Submit", command=update_current_profile(wb, ws, username))
    submit_current.pack()

    current_window.mainloop()
