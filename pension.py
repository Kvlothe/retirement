import tkinter as tk


def pension_input_window():
    global main_window
    pension_window = tk.Tk()
    pension_window.geometry("200x600")

    # Create Label and Entry for Pensions
    pension_63_label = tk.Label(window, text="63")
    pension_63_label.pack()
    pension_65_label = tk.Label(window, text="65")
    pension_65_label.pack()
    pension_lump_label = tk.Label(window, text="Lump")
    pension_lump_label.pack()
    pension_self_label = tk.Label(window, text="Self")
    pension_self_label.pack()
    pension_s1_63_entry = tk.Entry(window)
    pension_s1_63_entry.pack()
    pension_s1_65_entry = tk.Entry(window)
    pension_s1_65_entry.pack()
    pension_s1_lump_entry = tk.Entry(window)
    pension_s1_lump_entry.pack()
    pension_spouse_label = tk.Label(window, text="Spouse")
    pension_spouse_label.pack()
    pension_s2_63_entry = tk.Entry(window)
    pension_s2_63_entry.pack()
    pension_s2_65_entry = tk.Entry(window)
    pension_s2_65_entry.pack()
    pension_s2_lump_entry = tk.Entry(window)
    pension_s2_lump_entry.pack()

    submit_basic = tk.Button(pension_window, text="Submit", command=update_pension_info)
    submit_basic.pack()

    pension_window.mainloop()
    pension_window.destroy()
    main_menu_window()
