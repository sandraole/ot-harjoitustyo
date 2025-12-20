"""Rekisteröintisivu uuden käyttäjän luomista varten"""

import tkinter as tk
from tkinter import ttk, messagebox
from ui.theme import BG, CARD_BG, BORDER


class RegisterView(tk.Frame):
    """Näyttää lomakkeen uuden käyttäjän luomista varten.
    
    Attribute:
        _user_service: vastaa käyttäjän logiikasta
        _on_success: funktio, jota kutsutaan kun käyttäjä on luotu
        _on_cancel: funktio, jota kutsutaan kun palataan takaisin kirjautumisisvulle
    """

    def __init__(self, root, user_service, on_success, on_cancel):
        """"Luo rekisterlintisivun.
        
        Args: root: Tkinterin juuri
        user_service: vastaa käyttäjien käsittelystä
        on_success: funktio, jota kutsutaan kun käyttäjän luominen onnistuu
        on_cancel: funktio, jota kutsutaan kun käyttäjä palaa takaisin
        """
        super().__init__(root, padx=10, pady=10)

        self._user_service = user_service
        self._on_success = on_success
        self._on_cancel = on_cancel

        outer = tk.Frame(self, bg=BG)
        outer.pack(fill="both", expand=True)

        card = tk.Frame(
            outer,
            bg=CARD_BG,
            padx=20,
            pady=20,
            highlightbackground=BORDER,
            highlightthickness=2,
        )
        card.pack(expand=True, fill="both", padx=40, pady=40)

        title_label = tk.Label(
            card,
            text="Create account",
            font=("Arial", 18, "bold"),
            bg=CARD_BG,
            fg="black",
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        username_label = tk.Label(card, text="Username", bg=CARD_BG, fg="black")
        username_label.grid(row=1, column=0, sticky="w", pady=5)

        self._username_entry = ttk.Entry(card)
        self._username_entry.grid(row=1, column=1, sticky="ew", pady=5, padx=(8, 0))

        password_label = tk.Label(card, text="Password", bg=CARD_BG, fg="black")
        password_label.grid(row=2, column=0, sticky="w", pady=5)

        self._password_entry = ttk.Entry(card, show="*")
        self._password_entry.grid(row=2, column=1, sticky="ew", pady=5, padx=(8, 0))

        buttons_frame = tk.Frame(card, bg=CARD_BG)
        buttons_frame.grid(row=3, column=0, columnspan=2, pady=(15, 0), sticky="e")

        create_button = ttk.Button(
            buttons_frame,
            text="Create account",
            command=self._handle_create_user
        )
        create_button.grid(row=0, column=0, padx=(0, 8))

        cancel_button = ttk.Button(
            buttons_frame,
            text="Back to login",
            command=self._on_cancel
        )
        cancel_button.grid(row=0, column=1)

        card.grid_columnconfigure(1, weight=1)

    def _handle_create_user(self):
        """"On vastuussa uuden käyttäjän luomisesta.
        
        Jos kentät ovat tyhjiä, käyttäjä on jo olemassa tai käyttäjän
        luominen epäonnistuu --> näyttää virheilmoituksen.
        Kutsuu _on_success-callbackia, kun käyttäjän luominen onnistuu.
        """
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
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create user: {e}")
            return

        self._on_success()