# src/ui/register.py

import tkinter as tk
from tkinter import ttk, messagebox


class RegisterView(tk.Frame):
    def __init__(self, root, user_service, on_success, on_cancel):
        super().__init__(root, padx=10, pady=10)

        self._user_service = user_service
        self._on_success = on_success
        self._on_cancel = on_cancel

        title_label = tk.Label(
            self,
            text="Register",
            font=("Arial", 16)
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Username
        username_label = tk.Label(self, text="Username")
        username_label.grid(row=1, column=0, sticky="w", pady=5)

        self._username_entry = ttk.Entry(self)
        self._username_entry.grid(row=1, column=1, sticky="ew", pady=5)

        # Password
        password_label = tk.Label(self, text="Password")
        password_label.grid(row=2, column=0, sticky="w", pady=5)

        self._password_entry = ttk.Entry(self, show="*")
        self._password_entry.grid(row=2, column=1, sticky="ew", pady=5)

        # Buttons
        create_button = ttk.Button(
            self,
            text="Create account",
            command=self._handle_create_user
        )
        create_button.grid(row=3, column=0, pady=(10, 0))

        cancel_button = ttk.Button(
            self,
            text="Back to login",
            command=self._on_cancel
        )
        cancel_button.grid(row=3, column=1, pady=(10, 0))

        # layout joustavaksi
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

    def _handle_create_user(self):
        username = self._username_entry.get().strip()
        password = self._password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Username and password are required")
            return

        try:
            self._user_service.create_user(username, password)
        except ValueError:
            messagebox.showerror("Error", "User already exists")
            return
        except Exception as e:  # ei pakollinen, mutta kiva fallback
            messagebox.showerror("Error", f"Failed to create user: {e}")
            return

        # onnistui → takaisin login-näkymään
        self._on_success()
