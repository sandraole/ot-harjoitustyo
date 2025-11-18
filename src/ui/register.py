import tkinter as tk
from tkinter import ttk, messagebox
from services.user_service import user_service


class RegisterView(tk.Frame):
    def __init__(self, root, show_login_view):
        super().__init__(root, padx=10, pady=10)
        self._show_login_view = show_login_view

        tk.Label(self, text="Register", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="Username").pack()
        self._username_entry = ttk.Entry(self)
        self._username_entry.pack()

        tk.Label(self, text="Password").pack()
        self._password_entry = ttk.Entry(self, show="*")
        self._password_entry.pack()

        ttk.Button(self, text="Create Account",
                   command=self._register_user).pack(pady=5)

    def _back_to_login(self):
        self.destroy()
        self._show_login_view()

    def _register_user(self):
        try:
            user_service.create_user(
                self._username_entry.get(), self._password_entry.get())
            messagebox.showinfo("Success", "User created successfully!")
            self.destroy()
            self._show_login_view()
        except Exception as e:
            messagebox.showerror("Error", str(e))
