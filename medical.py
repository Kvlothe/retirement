import tkinter as tk


def update_medical_info(wb, ws, username):
    medical_info = medical_expense_entry.get()
    ws['C45'] = medical_info
    wb.save(f'{username}.xlsx')


def medical_window(medical_input_window, wb, ws, username):
    global medical_expense_entry

    # medical_input_window = tk.Tk()
    medical_input_window.geometry("100x50")

    # Create Label and Entry for Medical
    medical_expense_label = tk.Label(medical_input_window, text="Medical")
    medical_expense_label.pack()

    medical_expense_entry = tk.Entry(medical_input_window)
    medical_expense_entry.pack()

    submit_basic = tk.Button(medical_input_window, text="Submit", command=lambda: update_medical_info(wb, ws, username))
    submit_basic.pack()

    medical_input_window.mainloop()
