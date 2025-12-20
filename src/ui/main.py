"""Sovelluksen päänäkymä --> kirjalista."""

import tkinter as tk
from tkinter import messagebox
from ui.theme import BG, CARD_BG, BORDER


class MainView(tk.Frame):
    """"Kirjalistan näyttävä sivu.
    
    Näyttää kirjautuneelle käyttäjälle lomakkeen uuden kirjan lisäämisestä,
    sekä lukemattomat, että luetut kirjat.
    
    Attributes:
        _root: Tkniterin juuri.
        _username: käyttäjätunnus.
        _logout_handler: funktio, jota kutsutaan uloskirjautuessa.
        _book_service: vastaa kirjojen logiikasta.
        _books: viimeisimmät kirjat.
        _unread_indices: lista lukemattomien kirjojen indekseistä.
        _read_indices: lista luettujen kirjojen indekseistä.
    """

    def __init__(self, root, username, logout_handler, book_service):
        """Lue uuden MainView ikkunan.
        
        Args:
            root: Tkinterin juuri.
            username: käyttäjätunnus.
            logout_handler: funktio, jota kututaan uloskirjautuessa.
            book_service: vastaa kirjojen käsittelystä.
        """
        super().__init__(root, padx=10, pady=10, bg=BG)

        self._root = root
        self._username = username
        self._logout_handler = logout_handler
        self._book_service = book_service
        self._books = self._book_service.get_books()
        self._unread_indices = []
        self._read_indices = []

        title_label = tk.Label(
            self,
            text=f"Welcome to Book Tracker, {self._username}",
            font=("Arial", 18, "bold"),
            bg=BG,
            fg="black",
        )
        title_label.pack(pady=(0, 15), anchor="w")

        form_card = tk.Frame(
            self,
            bg=CARD_BG,
            padx=15,
            pady=15,
            highlightbackground=BORDER,
            highlightthickness=2,
        )
        form_card.pack(fill="x", pady=(0, 10))

        tk.Label(form_card, text="Title", bg=CARD_BG, fg="black").grid(
            row=0, column=0, sticky="w"
        )
        self._title_entry = tk.Entry(form_card, width=30)
        self._title_entry.grid(row=0, column=1, padx=(8, 0), sticky="ew")

        tk.Label(form_card, text="Author", bg=CARD_BG, fg="black").grid(
            row=1, column=0, sticky="w", pady=(5, 0)
        )
        self._author_entry = tk.Entry(form_card, width=30)
        self._author_entry.grid(row=1, column=1, padx=(8, 0), sticky="ew", pady=(5, 0))

        tk.Label(form_card, text="Pages", bg=CARD_BG, fg="black").grid(
            row=2, column=0, sticky="w", pady=(5, 0)
        )
        self._pages_entry = tk.Entry(form_card, width=10)
        self._pages_entry.grid(row=2, column=1, padx=(8, 0), sticky="w", pady=(5, 0))

        add_button = tk.Button(
            form_card,
            text="Add book",
            command=self._handle_add_book
        )
        add_button.grid(row=3, column=0, columnspan=2,
                        pady=(10, 0), sticky="ew")

        form_card.grid_columnconfigure(1, weight=1)

        lists_card = tk.Frame(
            self,
            bg=CARD_BG,
            padx=10,
            pady=10,
            highlightbackground=BORDER,
            highlightthickness=2,
        )
        lists_card.pack(fill="both", expand=True, pady=(10, 10))

        unread_frame = tk.Frame(lists_card, bg=CARD_BG)
        unread_frame.pack(fill="both", expand=True, pady=(0, 5))

        unread_label = tk.Label(
            unread_frame,
            text="Unread books",
            bg=CARD_BG,
            fg="black",
            font=("Arial", 12, "bold"),
        )
        unread_label.pack(anchor="w")

        self._unread_listbox = tk.Listbox(unread_frame, width=60, height=8)
        self._unread_listbox.pack(fill="both", expand=True, pady=(5, 0))

        # Luetut
        read_frame = tk.Frame(lists_card, bg=CARD_BG)
        read_frame.pack(fill="both", expand=True, pady=(5, 0))

        read_label = tk.Label(
            read_frame,
            text="Read books",
            bg=CARD_BG,
            fg="black",
            font=("Arial", 12, "bold"),
        )
        read_label.pack(anchor="w")

        self._read_listbox = tk.Listbox(read_frame, width=60, height=8)
        self._read_listbox.pack(fill="both", expand=True, pady=(5, 0))

        self._unread_listbox.bind("<Double-Button-1>", self._handle_toggle_read)
        self._read_listbox.bind("<Double-Button-1>", self._handle_toggle_read)

        bottom_frame = tk.Frame(self, bg=BG)
        bottom_frame.pack(fill="x")

        buttons_frame = tk.Frame(bottom_frame, bg=BG)
        buttons_frame.pack(side="left", anchor="w")

        delete_button = tk.Button(
            buttons_frame,
            text="Delete selected book",
            command=self._handle_delete_book
        )
        delete_button.pack(pady=(5, 0), anchor="w")

        logout_button = tk.Button(
            buttons_frame,
            text="Logout",
            command=self._logout_handler
        )
        logout_button.pack(pady=(10, 0), anchor="w")

        stats_frame = tk.Frame(bottom_frame, bg=BG)
        stats_frame.pack(side="right", anchor="e", padx=(0, 10), pady=(0, 5))

        self._read_count_var = tk.StringVar()
        self._total_count_var = tk.StringVar()
        self._read_percentage_var = tk.StringVar()

        tk.Label(stats_frame, textvariable=self._read_count_var, bg=BG, fg="black").pack(anchor="e")
        tk.Label(stats_frame, textvariable=self._total_count_var, bg=BG, fg="black").pack(anchor="e")
        tk.Label(stats_frame, textvariable=self._read_percentage_var, bg=BG, fg="black").pack(anchor="e")

        self._refresh_book_list()

    def _handle_add_book(self):
        """"Käsittelee uuden kirjan lisäämisen käyttöliittymästä."""
        title = self._title_entry.get()
        author = self._author_entry.get()
        pages = self._pages_entry.get()

        try:
            self._book_service.add_book(title, author, pages)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        self._books = self._book_service.get_books()
        self._refresh_book_list()

        self._title_entry.delete(0, tk.END)
        self._author_entry.delete(0, tk.END)
        self._pages_entry.delete(0, tk.END)

    def _handle_toggle_read(self, event):
        """Käsittelee kaksoisklikkauksen, joka siirtää kirjan luettu-tilaan.
        
        Args:
            event: Tkinterin tapahtumaolio, joka kertoo kummassa tilassa kirja on.
        """
        widget = event.widget

        if widget == self._unread_listbox:
            selection = self._unread_listbox.curselection()
            if not selection:
                return
            list_index = selection[0]
            book_index = self._unread_indices[list_index]
        elif widget == self._read_listbox:
            selection = self._read_listbox.curselection()
            if not selection:
                return
            list_index = selection[0]
            book_index = self._read_indices[list_index]
        else:
            return

        self._book_service.toggle_book_read(book_index)

        self._books = self._book_service.get_books()
        self._refresh_book_list()

    def _handle_delete_book(self):
        """Poistaa valitun kirjan halutusta listasta."""
        selection_unread = self._unread_listbox.curselection()
        selection_read = self._read_listbox.curselection()

        if selection_unread:
            list_index = selection_unread[0]
            book_index = self._unread_indices[list_index]
        elif selection_read:
            list_index = selection_read[0]
            book_index = self._read_indices[list_index]
        else:
            messagebox.showerror("Error", "Please select a book to delete")
            return

        confirm = messagebox.askyesno(
            "Confirm delete",
            "Are you sure you want to delete the selected book?"
        )
        if not confirm:
            return

        self._book_service.delete_book(book_index)

        self._books = self._book_service.get_books()
        self._refresh_book_list()

    def _refresh_book_list(self):
        """Päivittää molempien kirjojen listat."""
        self._unread_listbox.delete(0, tk.END)
        self._read_listbox.delete(0, tk.END)
        self._unread_indices = []
        self._read_indices = []

        for i, book in enumerate(self._books):
            if isinstance(book, dict):
                title = book.get("title", "")
                author = book.get("author", "")
                pages = book.get("pages", "")
                read = book.get("read", False)
                line = f"{title} — {author} ({pages} pages)"
            else:
                read = False
                line = str(book)

            if read:
                self._read_indices.append(i)
                self._read_listbox.insert(tk.END, line)
            else:
                self._unread_indices.append(i)
                self._unread_listbox.insert(tk.END, line)

        self._refresh_statistics()

    def _refresh_statistics(self):
        """Päivittää tilastotekstien sisällön."""
        stats = self._book_service.get_statistics()

        self._read_count_var.set(f"Read books: {stats['read_books']}")
        self._total_count_var.set(f"Total books: {stats['total_books']}")
        self._read_percentage_var.set(
            f"Read pages: {stats['read_page_percentage']:.1f}%"
        )
