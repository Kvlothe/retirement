import tkinter as tk


def update_pension_info(wb, ws, username):
    self_pension_63 = pension_s1_63_entry.get()
    self_pension_65 = pension_s1_65_entry.get()
    self_pension_lump = pension_s1_lump_entry.get()
    spouse_pension_63 = pension_s2_63_entry.get()
    spouse_pension_65 = pension_s2_65_entry.get()
    spouse_pension_lump = pension_s2_lump_entry.get()

    ws['C22'] = self_pension_63
    ws['D22'] = self_pension_65
    ws['E22'] = self_pension_lump
    ws['C23'] = spouse_pension_63
    ws['D23'] = spouse_pension_65
    ws['E23'] = spouse_pension_lump

    wb.save(f'{username}.xlsx')


def pension_input_window(pension_window, wb, ws, username):
    global pension_s1_63_entry, pension_s1_65_entry, pension_s1_lump_entry, pension_s2_63_entry, pension_s2_65_entry, pension_s2_lump_entry
    pension_window.geometry("200x400")

    # Create Label and Entry for Pensions
    pension_self_label = tk.Label(pension_window, text="Self")
    pension_self_label.pack()
    pension_63_label = tk.Label(pension_window, text="63")
    pension_63_label.pack()
    pension_s1_63_entry = tk.Entry(pension_window)
    pension_s1_63_entry.pack()
    pension_65_label = tk.Label(pension_window, text="65")
    pension_65_label.pack()
    pension_s1_65_entry = tk.Entry(pension_window)
    pension_s1_65_entry.pack()
    pension_lump_label = tk.Label(pension_window, text="Lump")
    pension_lump_label.pack()
    pension_s1_lump_entry = tk.Entry(pension_window)
    pension_s1_lump_entry.pack()
    pension_spouse_label = tk.Label(pension_window, text="Spouse")
    pension_spouse_label.pack()
    spouse_pension_63_label = tk.Label(pension_window, text="63")
    spouse_pension_63_label.pack()
    pension_s2_63_entry = tk.Entry(pension_window)
    pension_s2_63_entry.pack()
    spouse_pension_65_label = tk.Label(pension_window, text="65")
    spouse_pension_65_label.pack()
    pension_s2_65_entry = tk.Entry(pension_window)
    pension_s2_65_entry.pack()
    spouse_pension_lump_label = tk.Label(pension_window, text="Lump")
    spouse_pension_lump_label.pack()
    pension_s2_lump_entry = tk.Entry(pension_window)
    pension_s2_lump_entry.pack()

    submit_basic = tk.Button(pension_window, text="Submit", command=update_pension_info(wb, ws, username))
    submit_basic.pack()

    pension_window.mainloop()
