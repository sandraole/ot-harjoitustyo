import tkinter as tk
from tkinter import ttk, messagebox
from services.user_service import user_service
from .register import RegisterView
from .main import MainView


class UI:

    def __init__(self, root):
        self._root = root
        self._frame = None

    def start(self):
        self._show_login_view()

    def _show_login_view(self):
        if self._frame:
            self._frame.destroy()

        self._frame = tk.Frame(
            master=self._root, bg="#3498db", padx=10, pady=10)
        self._frame.pack(fill="both", expand=True)

        tk.Label(self._frame, text="Login", font=("Arial", 16),
                 bg="#3498db", fg="white").pack(pady=10)

        tk.Label(self._frame, text="Username", bg="#3498db", fg="white").pack()
        username_entry = ttk.Entry(self._frame)
        username_entry.pack()

        tk.Label(self._frame, text="Password", bg="#3498db", fg="white").pack()
        password_entry = ttk.Entry(self._frame, show="*")
        password_entry.pack()

        ttk.Button(self._frame, text="Sign In", command=lambda: self._sign_in(
            username_entry.get(), password_entry.get())).pack(pady=5)
        ttk.Button(self._frame, text="Register",
                   command=self._show_register_view).pack()

    def _sign_in(self, username, password):
        if user_service.authenticate(username, password):
            if self._frame:
                self._frame.destroy()

            self._frame = MainView(self._root)
            self._frame.pack(fill="both", expand=True)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def _show_register_view(self):
        if self._frame:
            self._frame.destroy()

        self._frame = RegisterView(self._root, self.start)
        self._frame.pack(fill="both", expand=True)
