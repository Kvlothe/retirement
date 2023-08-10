import tkinter as tk


def update_assumptions(wb, ws, username):
    inflation = inflation_entry.get()
    cost_70 = cost_of_living_70_entry.get()
    cost_85 = cost_of_living_85_entry.get()
    social_cola = social_cola_entry.get()
    medicare_65 = medicare_65_entry.get()

    inflation_value = float(inflation) if inflation else 0.0
    cost_70_value = float(cost_70) if cost_70 else 0.0
    cost_85_value = float(cost_85) if cost_85 else 0.0
    social_cola_value = float(social_cola) if social_cola else 0.0
    medicare_65_value = float(medicare_65) if medicare_65 else 0.0

    ws['C49'] = inflation_value / 100
    ws['C50'] = cost_70_value / 100
    ws['C51'] = cost_85_value / 100
    ws['C52'] = social_cola_value / 100
    ws['C53'] = medicare_65_value / 100


class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)

    def enter(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip, text=self.text, bg="yellow", relief=tk.SOLID, borderwidth=1)
        label.pack(ipadx=1)

    def leave(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()


def assumptions_window(assumptions_input_window, wb, ws, username):
    global inflation_entry, cost_of_living_70_entry, cost_of_living_85_entry, social_cola_entry, medicare_65_entry

    assumptions_input_window.geometry("250x220")

    inflation_value = ws['C49'].value if ws['C49'].value else ""
    cost_70_value = ws['C50'].value if ws['C50'].value else ""
    cost_85_value = ws['C51'].value if ws['C51'].value else ""
    social_cola_value = ws['C52'].value if ws['C52'].value else ""
    medicare_65_value = ws['C53'].value if ws['C53'].value else ""

    inflation_label = tk.Label(assumptions_input_window, text="Inflation")
    inflation_label.pack()
    inflation_entry = tk.Entry(assumptions_input_window)
    inflation_entry.insert(0, inflation_value)
    inflation_entry.pack()
    cost_of_living_70_label = tk.Label(assumptions_input_window, text="Estimated Cost of living reduction at 70")
    cost_of_living_70_label.pack()
    cost_of_living_70_entry = tk.Entry(assumptions_input_window)
    cost_of_living_70_entry.insert(0, cost_70_value)
    cost_of_living_70_entry.pack()
    cost_of_living_85_label = tk.Label(assumptions_input_window, text="Estimated Cost of living increase at 85")
    cost_of_living_85_label.pack()
    cost_of_living_85_entry = tk.Entry(assumptions_input_window)
    cost_of_living_85_entry.insert(0, cost_85_value)
    cost_of_living_85_entry.pack()
    social_cola_label = tk.Label(assumptions_input_window, text="Social Security COLA, Estimated")
    social_cola_label.pack()
    social_cola_entry = tk.Entry(assumptions_input_window)
    social_cola_entry.insert(0, social_cola_value)
    social_cola_entry.pack()
    medicare_65_label = tk.Label(assumptions_input_window, text="Estimated Save with Medicare at 65")
    medicare_65_label.pack()
    medicare_65_entry = tk.Entry(assumptions_input_window)
    medicare_65_entry.insert(0, medicare_65_value)
    medicare_65_entry.pack()

    ToolTip(inflation_entry, "Enter Inflation(ref tab)")
    ToolTip(cost_of_living_70_entry, "Enter cost of living at age 70, suggestion that expense at 75 reduce by 10%")
    ToolTip(cost_of_living_85_entry, "Enter cost of living at age 85, if long term care insurance may not need this, but assume cost of living increase as we age")
    ToolTip(social_cola_entry, "Enter social security COLA, typically matches inflation")
    ToolTip(medicare_65_entry, "Enter estimated save with Medicare at 65, assuming half cost before Medicare, should be much less")

    submit_button = tk.Button(assumptions_input_window, text="Submit", command=lambda: update_assumptions(wb, ws, username))
    submit_button.pack()

    assumptions_input_window.mainloop()
