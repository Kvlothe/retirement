import tkinter as tk


def assumptions_window(assumptions_input_window, wb, ws, username):
    # global

    # assumptions_input_window = tk.Tk()
    assumptions_input_window.geometry("250x220")

    inflation_label = tk.Label(assumptions_input_window, text="Inflation")
    inflation_label.pack()
    inflation_entry = tk.Entry(assumptions_input_window)
    inflation_entry.pack()
    cost_of_living_70_label = tk.Label(assumptions_input_window, text="Estimated Cost of living reduction at 70")
    cost_of_living_70_label.pack()
    cost_of_living_70_entry = tk.Entry(assumptions_input_window)
    cost_of_living_70_entry.pack()
    cost_of_living_85_label = tk.Label(assumptions_input_window, text="Estimated Cost of living increase at 85")
    cost_of_living_85_label.pack()
    cost_of_living_85_entry = tk.Entry(assumptions_input_window)
    cost_of_living_85_entry.pack()
    social_cola_label = tk.Label(assumptions_input_window, text="Social Security COLA, Estimated")
    social_cola_label.pack()
    social_cola_entry = tk.Entry(assumptions_input_window)
    social_cola_entry.pack()
    medicare_65_label = tk.Label(assumptions_input_window, text="Estimated Save with Medicare at 65")
    medicare_65_label.pack()
    medicare_65_entry = tk.Entry(assumptions_input_window)
    medicare_65_entry.pack()

    assumptions_input_window.mainloop()
