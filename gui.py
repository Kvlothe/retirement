import tkinter as tk


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.button = tk.Button(self.root, text="Open", command=self.open_other_window)
        self.button.pack()

    def open_other_window(self):
        self.root.withdraw()
        top = tk.Toplevel(self.root)
        other_window = OtherWindow(top)


class OtherWindow:
    def __init__(self, root):
        self.root = root
        self.button = tk.Button(self.root, text="Close", command=self.close)
        self.button.pack()

    def close(self):
        self.root.destroy()