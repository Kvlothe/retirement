import tkinter as tk


def update_growth_investment_info(wb, ws, username):
    stock_asset = stock_asset_entry.get()
    bonds_asset = bonds_asset_entry.get()
    cash_asset = cash_asset_entry.get()
    stock_average = stock_average_entry.get()
    stock_stdev = stock_stdev_entry.get()
    bonds_average = bonds_average_entry.get()
    bonds_stdev = bonds_stdev_entry.get()
    cash_average = cash_average_entry.get()
    cash_stdev = cash_stdev_entry.get()

    # Convert the input to a float value representing the percentage
    stock_percentage_value = float(stock_asset) if stock_asset else 0.0
    bonds_percentage_value = float(bonds_asset) if bonds_asset else 0.0
    cash_percentage_value = float(cash_asset) if cash_asset else 0.0
    stock_average_percentage_value = float(stock_average) if stock_average else 0.0
    stock_stdev_percentage_value = float(stock_stdev) if stock_stdev else 0.0
    bonds_average_percentage_value = float(bonds_average) if bonds_average else 0.0
    cash_average_percentage_value = float(cash_average) if cash_average else 0.0
    bonds_stdev_percentage_value = float(bonds_stdev) if bonds_stdev else 0.0
    cash_stdev_percentage_value = float(cash_stdev) if cash_stdev else 0.0

    ws['C58'] = stock_percentage_value / 100
    ws['E58'] = stock_average_percentage_value / 100
    ws['E59'] = stock_stdev_percentage_value / 100
    ws['C60'] = bonds_percentage_value / 100
    ws['E60'] = bonds_average_percentage_value / 100
    ws['E61'] = bonds_stdev_percentage_value / 100
    ws['C62'] = cash_percentage_value / 100
    ws['E62'] = cash_average_percentage_value / 100
    ws['E63'] = cash_stdev_percentage_value / 100

    wb.save(f'{username}.xlsx')


def growth_and_assumptions_window(growth_window, wb, ws, username):
    global stock_asset_entry, bonds_asset_entry, cash_asset_entry, stock_average_entry, stock_stdev_entry, bonds_average_entry, bonds_stdev_entry, cash_average_entry, cash_stdev_entry

    growth_window.geometry("400x400")
    stock_asset_value = ws['C58'].value if ws['C58'].value else ""
    stock_average_value = ws['E58'].value if ws['E58'].value else ""
    stock_stdev_value = ws['E59'].value if ws['E59'].value else ""
    bonds_asset_value = ws['C60'].value if ws['C60'].value else ""
    bonds_average_value = ws['E60'].value if ws['E60'].value else ""
    bonds_stdev_value = ws['E61'].value if ws['E61'].value else ""
    cash_asset_value = ws['C62'].value if ws['C62'].value else ""
    cash_average_value = ws['E62'].value if ws['E62'].value else ""
    cash_stdev_value = ws['E63'].value if ws['E63'].value else ""

    stock_asset_label = tk.Label(growth_window, text="Stock asset")
    stock_average_label = tk.Label(growth_window, text="Stock Average")
    stock_stdev_label = tk.Label(growth_window, text="Stock STDEV")
    stock_asset_label.pack()
    stock_asset_entry = tk.Entry(growth_window)
    stock_asset_entry.insert(0, stock_asset_value)
    stock_asset_entry.pack()
    stock_average_label.pack()
    stock_average_entry = tk.Entry(growth_window)
    stock_average_entry.insert(0, stock_average_value)
    stock_average_entry.pack()
    stock_stdev_label.pack()
    stock_stdev_entry = tk.Entry(growth_window)
    stock_stdev_entry.insert(0, stock_stdev_value)
    stock_stdev_entry.pack()

    bonds_asset_label = tk.Label(growth_window, text="Bonds Asset")
    bonds_average_label = tk.Label(growth_window, text="Bonds Average")
    bonds_stdev_label = tk.Label(growth_window, text="Bonds STDEV")
    bonds_asset_entry = tk.Entry(growth_window)
    bonds_asset_entry.insert(0, bonds_asset_value)
    bonds_asset_label.pack()
    bonds_asset_entry.pack()
    bonds_average_entry = tk.Entry(growth_window)
    bonds_average_entry.insert(0, bonds_average_value)
    bonds_average_label.pack()
    bonds_average_entry.pack()
    bonds_stdev_entry = tk.Entry(growth_window)
    bonds_stdev_label.pack()
    bonds_stdev_entry.insert(0, bonds_stdev_value)
    bonds_stdev_entry.pack()

    cash_average_label = tk.Label(growth_window, text="Cash Average")
    cash_asset_label = tk.Label(growth_window, text='Cash Asset')
    cash_stdev_label = tk.Label(growth_window, text="Cash STDEV")
    cash_asset_label.pack()
    cash_asset_entry = tk.Entry(growth_window)
    cash_asset_entry.insert(0, cash_asset_value)
    cash_asset_entry.pack()
    cash_average_label.pack()
    cash_average_entry = tk.Entry(growth_window)
    cash_average_entry.insert(0, cash_average_value)
    cash_average_entry.pack()
    cash_stdev_entry = tk.Entry(growth_window)
    cash_stdev_label.pack()
    cash_stdev_entry.insert(0, cash_stdev_value)
    cash_stdev_entry.pack()

    submit_button = tk.Button(growth_window, text="Submit", command=lambda: update_growth_investment_info(wb, ws, username))
    submit_button.pack()

    growth_window.mainloop()

