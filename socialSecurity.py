import tkinter as tk


def update_social_info(wb, ws, username):
    ss1 = ss_s1_entry.get()
    ss2 = ss_s2_entry.get()

    ws['C18'] = ss1
    ws['C19'] = ss2

    wb.save(f'{username}.xlsx')


def social_security_window(security_window, wb, ws, username):
    global main_window, ss_s1_entry, ss_s2_entry

    # security_window = tk.Tk()
    security_window.geometry("200x120")

    # Create Label and Entry for Social Security
    ss_s1_label = tk.Label(security_window, text="Self")
    ss_s1_label.pack()
    ss_s1_entry = tk.Entry(security_window)
    ss_s1_entry.pack()
    ss_s2_label = tk.Label(security_window, text="Spouse")
    ss_s2_label.pack()
    ss_s2_entry = tk.Entry(security_window)
    ss_s2_entry.pack()

    submit_basic = tk.Button(security_window, text="Submit", command=update_social_info(wb, ws, username))
    submit_basic.pack()

    security_window.mainloop()
