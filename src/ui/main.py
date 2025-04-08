import tkinter as tk

class MainView(tk.Frame):
    def __init__(self, root):
        super().__init__(root, padx=10, pady=10)

        tk.Label(self, text="Welcome to your Budget!", font=("Arial", 16)).pack()