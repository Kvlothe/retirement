import os
import tkinter as tk
from basicInfo import basic_info_window
from currentProfile import current_profile_window
from socialSecurity import social_security_window
from pension import pension_input_window
import openpyxl


# Method for Loading or Creating a Profile
class LoadCreateWindow:
    def __init__(self, root):
        self.root = root
        # Create the label, entry and button
        self.name_label = tk.Label(self.root, text="Name")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.load_button = tk.Button(self.root, text="Load or Create Profile", command=self.load_or_create_profile)
        self.load_button.pack()

    def load_or_create_profile(self):
        # global wb, ws, username  # declare them as global so we can access them later
        username = self.name_entry.get()
        filename = f'{username}.xlsx'
        if os.path.exists(filename):
            wb = openpyxl.load_workbook(filename)
            print(f"Loaded existing profile for {username}")
        else:
            wb = openpyxl.load_workbook('Sample.xlsx')
            print(f"Created new profile for {username}")
        ws = wb.active
        self.root.destroy()  # This will close the current window
        main_window = MainWindow(tk.Tk(), wb, ws, username)  # This will open a new window


# Class for the Main Menu Window
class MainWindow:
    def __init__(self, root, wb, ws, username):
        self.root = root
        self.wb = wb
        self.ws = ws
        self.username = username
        self.basic_button = tk.Button(self.root, text="Basic Information", command=self.open_basic_window)
        self.basic_button.pack()
        self.profile_button = tk.Button(self.root, text='Current Profile', command=self.open_current_profile_window)
        self.profile_button.pack()
        self.social_button = tk.Button(self.root, text="Social Security", command=self.open_social_window)
        self.social_button.pack()
        self.pension_button = tk.Button(self.root, text="Pension", command=self.open_pension_window)
        self.pension_button.pack()
        self.inputs_button = tk.Button(self.root, text="Estimated Expenses ", command=self.open_inputs_window)
        self.inputs_button.pack()
        self.one_time_button = tk.Button(self.root, text="One Time Expenses", command=self.open_one_time_window)
        self.one_time_button.pack()
        self.medical_button = tk.Button(self.root, text="Medical", command=self.open_medical_window)
        self.medical_button.pack()
        self.assumptions_button = tk.Button(self.root, text="Assumptions", command=self.open_assumptions_window)
        self.assumptions_button.pack()

# Method for Basic Information Window
    def open_basic_window(self):
        basic_window = tk.Toplevel(self.root)
        basic_info_window(basic_window, self.wb, self.ws, self.username)

# Method for the Current Profile Window
    def open_current_profile_window(self):
        profile_window = tk.Toplevel(self.root)
        current_profile_window(profile_window, self.wb, self.ws, self.username)

# Method for the Pension Window
    def open_pension_window(self):
        pensions_window = tk.Toplevel(self.root)
        pension_input_window(pensions_window, self.wb, self.ws, self.username)

# Method for the Social Security Window
    def open_social_window(self):
        social_window = tk.Toplevel(self.root)
        social_security_window(social_window, self.wb, self.ws, self.username)

# Method for the Estimated Expenses (inputs) Window
    def open_inputs_window(self):
        input_window = tk.Toplevel(self.root)
        inputs_window(input_window, self.wb, self.ws, self.username)

# Method for the One Time Expenses Window
    def open_one_time_window(self):
        one_time_expense_window = tk.Toplevel(self.root)
        one_time_window(one_time_expense_window, self.wb, self.ws, self.username)

# Method for the Other Assumptions Window
    def open_assumptions_window(self):
        other_assumptions_window = tk.Toplevel(self.root)
        assumptions_window(other_assumptions_window, self.wb, self.ws, self.username)

# Method for the Medical Window
    def open_medical_window(self):
        medical_input_window = tk.Toplevel(self.root)
        medical_window(medical_input_window, self.wb, self.ws, self.username)

# Method for closing windows
    def close(self):
        self.root.master.deiconify()
        self.root.destroy()


# Class for the Basic Information Window
class BasicWindow:
    def __init__(self, root):
        self.root = root
        basic_info_window(self.root)
        self.button = tk.Button(self.root, text="Close", command=self.close)
        self.button.pack()

    def close(self):
        self.root.master.deiconify()
        self.root.destroy()


# Class for the Current Profile Window
class CurrentProfileWindow:
    def __init__(self, root):
        self.root = root
        current_profile_window(self.root)
        self.button = tk.Button(self.root, text="Close", command=self.close)
        self.button.pack()

    def close(self):
        self.root.master.deiconify()
        self.root.destroy()


# Class for the Social Security Window
class SocialWindow:
    def __init__(self, root):
        self.root = root
        social_security_window(self.root)
        self.button = tk.Button(self.root, text="Close", command=self.close)
        self.button.pack()

    def close(self):
        self.root.master.deiconify()
        self.root.destroy()


# Class for the Pension Window
class PensionWindow:
    def __init__(self, root):
        self.root = root
        pension_input_window(self.root)
        self.button = tk.Button(self.root, text="Close", command=self.close)
        self.button.pack()

    def close(self):
        self.root.master.deiconify()
        self.root.destroy()


# Class for the Estimated Expenses Window
class InputsWindow:
    def __init__(self, root):
        self.root = root
        inputs_window(self.root)
        self.button = tk.Button(self.root, text="Close", command=self.close)
        self.button.pack()

    def close(self):
        self.root.master.deiconify()
        self.root.destroy()


# Class for the One Time Expenses Window
class OneTimeWindow:
    def __init__(self, root):
        self.root = root
        one_time_window(self.root)
        self.button = tk.Button(self.root, text="Close", command=self.close)
        self.button.pack()

    def close(self):
        self.root.master.deiconify()
        self.root.destroy()


# Class for the medical Window
class MedicalWindow:
    def __init__(self, root):
        self.root = root
        medical_window(self.root)
        self.button = tk.Button(self.root, text="Close", command=self.close)
        self.button.pack()

    def close(self):
        self.root.master.deiconify()
        self.root.destroy()


# Class for the Assumptions Window
class AssumptionsWindow:
    def __init__(self, root):
        self.root = root
        assumptions_window(self.root)
        self.button = tk.Button(self.root, text="Close", command=self.close)
        self.button.pack()

    def close(self):
        self.root.master.deiconify()
        self.root.destroy()
