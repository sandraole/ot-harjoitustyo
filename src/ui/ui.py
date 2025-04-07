import tkinter as tk
from tkinter import ttk


class UI:

    def __init__(self, root):
        self._root = root
        self._frame = None

    def start(self):
        self._show_main_view()

    def _show_main_view(self):
        if self._frame:
            self._frame.destroy()

        self._frame = tk.Frame(master=self._root, bg="#3498db", padx=10, pady=10)
        self._frame.pack(fill="both", expand=True)

        heading_label = tk.Label(
            self._frame, text="Budgeting Application", font=("Arial", 16), bg="#3498db", fg="white"
        )
        heading_label.pack(pady=10)

        # Username
        username_label = tk.Label(
            self._frame, text="Username:", bg="#3498db", fg="white"
        )
        username_label.place(relx=0.1, rely=0.2)

        username_entry = ttk.Entry(self._frame)
        username_entry.place(relx=0.3, rely=0.2, relwidth=0.6)

        # Password
        password_label = tk.Label(
            self._frame, text="Password:", bg="#3498db", fg="white"
        )
        password_label.place(relx=0.1, rely=0.3)

        password_entry = ttk.Entry(self._frame, show="*")
        password_entry.place(relx=0.3, rely=0.3, relwidth=0.6)

        # Register button
        register_button = ttk.Button(self._frame, text="Register")
        register_button.place(relx=0.3, rely=0.45, relwidth=0.28)

        # Sign In button
        signin_button = ttk.Button(self._frame, text="Sign In")
        signin_button.place(relx=0.62, rely=0.45, relwidth=0.28)