""""Vastaa sovelluksen pääkäyttöliittymästä."""

import tkinter as tk
from tkinter import ttk, messagebox
from ui.main import MainView
from ui.register import RegisterView
from services.book_service import BookService
from repositories.book_repository import BookRepository
from ui.theme import BG, CARD_BG, BORDER


class UI:
    """"Luokka joka vatsaa sovelluksen näkymisen hallinnasta.
    
    Vastaa kirjautuimisen, rekisteröinnin, kirjalistan näyttämisestä ja
    vaihtamisesta.
    
    Attributes:
        _root: Tkinterion pääikkuna.
        _user_service: vastaa käyttäjiin liittyvästä logiikasta.
        _current_view: näkyvissä oleva Tkinter ikkuna.
    """
    def __init__(self, root, user_service):
        """Luo uuden UI-olion.
        
        Args:
            root: Tkinterin juuri ikkuna.
            user_service: vastaa käyttäjien käsittelystä.
        """
        self._root = root
        self._user_service = user_service
        self._current_view = None

    def start(self):
        """Käynnistää käyttliittymän näyttämällä kirjautumisnäkymän."""
        self._show_login_view()

    def _clear_current_view(self):
        """Tuhoaa nykyisen näkymän, jos sellainen on luotu."""
        if self._current_view is not None:
            self._current_view.destroy()
            self._current_view = None

    def _show_login_view(self):
        """Näyttää kirjautumissivun."""
        self._clear_current_view()

        outer = tk.Frame(self._root, bg=BG)
        outer.pack(fill="both", expand=True)
        self._current_view = outer

        card = tk.Frame(
            outer,
            bg=CARD_BG,
            padx=20,
            pady=20,
            highlightbackground=BORDER,
            highlightthickness=2,
        )
        card.pack(expand=True, fill="both", padx=40, pady=40)

        tk.Label(
            card,
            text="Login",
            font=("Arial", 18, "bold"),
            bg=CARD_BG,
            fg="black",
        ).pack(pady=(0, 15))

        form_frame = tk.Frame(card, bg=CARD_BG)
        form_frame.pack(fill="x")

        tk.Label(form_frame, text="Username", bg=CARD_BG, fg="black").grid(
            row=0, column=0, sticky="w", pady=(0, 8)
        )
        username_entry = ttk.Entry(form_frame)
        username_entry.grid(row=0, column=1, sticky="ew", pady=(0, 8), padx=(8, 0))

        tk.Label(form_frame, text="Password", bg=CARD_BG, fg="black").grid(
            row=1, column=0, sticky="w", pady=(0, 8)
        )
        password_entry = ttk.Entry(form_frame, show="*")
        password_entry.grid(row=1, column=1, sticky="ew", pady=(0, 8), padx=(8, 0))

        form_frame.grid_columnconfigure(1, weight=1)

        buttons_frame = tk.Frame(card, bg=CARD_BG)
        buttons_frame.pack(fill="x", pady=(10, 0))

        ttk.Button(
            buttons_frame,
            text="Sign In",
            command=lambda: self._sign_in(
                username_entry.get(),
                password_entry.get()
            )
        ).grid(row=0, column=0, padx=(0, 8))

        ttk.Button(
            buttons_frame,
            text="Register",
            command=self._show_register_view
        ).grid(row=0, column=1)

    def _sign_in(self, username, password):
        """Käsittelee kirjautumisnapin painamisen.
        
        Kursuu UserSerice.login metodia ja näyttää virheilmoituksen,
        jos kirjauminen epäonnistuu.
        
        Args:
            username: käyttäjätunnus.
            password: salasana.
        """
        try:
            logged_in_username = self._user_service.login(username, password)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        self._show_main_view(logged_in_username)

    def _show_main_view(self, username):
        """Näyttää kirjalistan kirjautuneelle käyttäjälle.
        
        Luo käyttäjäkohtaisen näkymän omista kirjoista.
        
        Args:
            username: käyttäjätunnus.
        """
        self._clear_current_view()

        def logout_handler():
            self.start()

        safe_username = username.replace(" ", "_")
        file_path = f"data/{safe_username}_books.json"

        book_repository = BookRepository(file_path=file_path)
        book_service = BookService(book_repository=book_repository)

        main_view = MainView(
            root=self._root,
            username=username,
            logout_handler=logout_handler,
            book_service=book_service,
        )

        main_view.pack(fill="both", expand=True)
        self._current_view = main_view

    def _show_register_view(self):
        """Näyttää uuden käyttäjän rekisteröintisivun."""
        self._clear_current_view()

        def on_success():
            messagebox.showinfo("Success", "User created, you can log in now")
            self.start()

        def on_cancel():
            self.start()

        register_view = RegisterView(
            root=self._root,
            user_service=self._user_service,
            on_success=on_success,
            on_cancel=on_cancel,
        )

        register_view.pack(fill="both", expand=True)
        self._current_view = register_view
