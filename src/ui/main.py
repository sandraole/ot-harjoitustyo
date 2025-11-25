import tkinter as tk
from tkinter import messagebox


class MainView(tk.Frame):
    def __init__(self, root):
        super().__init__(root, padx=10, pady=10)
        self.pack()

        tk.Label(self, text="Welcome to Book Tracker",
                 font=("Arial", 16)).pack(pady=5)

        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

    def start(self):
        """Käynnistää käyttöliittymän."""
        self._show_login_view()
