import tkinter as tk


def update_social_info():
    global main_window
    ss1 = ss_s1_entry.get()
    ss2 = ss_s2_entry.get()

    wb.save(f'{username}.xlsx')
    security_window.destroy()  # Close the basic info window
    main_menu_window()  # Open the main menu again


def social_security_window(window, wb, ws, username):
    global main_window, ss_s1_entry, ss_s2_entry
    security_window = tk.Toplevel(main_window)
    security_window.geometry("200x600")

    # Create Label and Entry for Social Security
    ss_s1_label = tk.Label(security_window, text="Self")
    ss_s1_label.pack()
    ss_s1_entry = tk.Entry(security_window)
    ss_s1_entry.pack()
    ss_s2_label = tk.Label(security_window, text="Spouse")
    ss_s2_label.pack()
    ss_s2_entry = tk.Entry(security_window)
    ss_s1_entry.pack()

    submit_basic = tk.Button(security_window, text="Submit", command=update_social_info)
    submit_basic.pack()

    security_window.mainloop()
