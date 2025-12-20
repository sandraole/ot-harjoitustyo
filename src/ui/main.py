"""Sovelluksen päänäkymä --> kirjalista."""

import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import messagebox
from ui.theme import BG, CARD_BG, BORDER, LINK


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
        _search_var: hakukentän teksti.
        _current_filter: viimeisenä käytetty hakusuodatin.
        _read_count_var: näyttää kaikki luetut kirjat.
        _total_count_var: näyttää kaikki kirjat.
        _read_pages_var: näyttää luetut sivut tai prosenttiosuudet.
        _show_read_percentage: totuusarvo, joka kertoo näyetäänkö sivut prosentteina vai sivuina.
        _last_stats: viimeisin haettu tilastosanakirja.
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
        self._search_var = tk.StringVar()
        self._current_filter = ""

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
        self._author_entry.grid(row=1, column=1, padx=(
            8, 0), sticky="ew", pady=(5, 0))

        tk.Label(form_card, text="Pages", bg=CARD_BG, fg="black").grid(
            row=2, column=0, sticky="w", pady=(5, 0)
        )
        self._pages_entry = tk.Entry(form_card, width=10)
        self._pages_entry.grid(row=2, column=1, padx=(
            8, 0), sticky="w", pady=(5, 0))

        add_button = tk.Button(
            form_card,
            text="Add book",
            command=self._handle_add_book
        )
        add_button.grid(row=3, column=0, columnspan=2,
                        pady=(10, 0), sticky="ew")

        form_card.grid_columnconfigure(1, weight=1)

        search_frame = tk.Frame(self, bg=BG)
        search_frame.pack(fill="x", pady=(0, 5))

        tk.Label(
            search_frame,
            text="Search (title or author):",
            bg=BG,
            fg="black"
        ).pack(side="left")

        search_entry = tk.Entry(
            search_frame, textvariable=self._search_var, width=30)
        search_entry.pack(side="left", padx=(5, 0))

        search_button = tk.Button(
            search_frame,
            text="Search",
            command=self._handle_search
        )
        search_button.pack(side="left", padx=(5, 0))

        clear_button = tk.Button(
            search_frame,
            text="Clear",
            command=self._handle_clear_search
        )
        clear_button.pack(side="left", padx=(5, 0))

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

        self._unread_listbox.bind(
            "<Double-Button-1>", self._handle_toggle_read)
        self._read_listbox.bind("<Double-Button-1>", self._handle_toggle_read)

        hint_label = tk.Label(
            self,
            text="Double-click a book to mark as read/unread",
            bg=BG,
            fg="black",
            font=("Arial", 10),
        )
        hint_label.pack(anchor="w", padx=(2, 0), pady=(0, 5))

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

        chart_button = tk.Button(
            stats_frame,
            text="Show reading chart",
            command=self._handle_show_chart,
        )
        chart_button.pack(anchor="e", pady=(0, 5))

        self._read_count_var = tk.StringVar()
        self._total_count_var = tk.StringVar()

        self._read_pages_var = tk.StringVar()
        self._show_read_percentage = True

        tk.Label(
            stats_frame,
            textvariable=self._read_count_var,
            bg=BG,
            fg="black"
        ).pack(anchor="e")

        tk.Label(
            stats_frame,
            textvariable=self._total_count_var,
            bg=BG,
            fg="black"
        ).pack(anchor="e")

        read_pages_label = tk.Label(
            stats_frame,
            textvariable=self._read_pages_var,
            bg=BG,
            fg=LINK,
            font=("Arial", 11, "underline"),
            cursor="hand2",
        )
        read_pages_label.pack(anchor="e")

        read_pages_label.bind("<Button-1>", self._toggle_read_pages_view)

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

    def _handle_search(self):
        """Suodattaa kirjalistan hakutekstin perusteella."""
        self._current_filter = self._search_var.get().strip().lower()
        self._refresh_book_list()

        if self._current_filter and not self._unread_indices and not self._read_indices:
            messagebox.showinfo(
                "No books found", "No books match your search.")

    def _handle_clear_search(self):
        """Tyhjentää haun ja näyttää kaikki kirjat."""
        self._search_var.set("")
        self._current_filter = ""
        self._refresh_book_list()

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
                title = ""
                author = ""
                read = False
                line = str(book)

            if self._current_filter:
                haystack = f"{title} {author}".lower()
                if self._current_filter not in haystack:
                    continue

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
        self._last_stats = stats

        self._read_count_var.set(f"Read books: {stats['read_books']}")
        self._total_count_var.set(f"Total books: {stats['total_books']}")

        self._update_read_pages_text()

    def _toggle_read_pages_view(self, event=None):
        """Vaihtaa luettujen sivujen näkymän (prosentti <-> sivumäärä).
        Args: 
            event: Tkinterin tapahtumaolio. Ei käytetä, mutta mukana, että
            metodia pystytään kutsuman klikatessa.

        """
        self._show_read_percentage = not self._show_read_percentage
        self._update_read_pages_text()

    def _update_read_pages_text(self):
        """Päivittää luettujen sivujen tekstin valitun näkymän mukaan."""
        stats = self._last_stats

        if self._show_read_percentage:
            text = f"Read pages: {stats['read_page_percentage']:.1f}%"
        else:
            text = f"Read pages: {stats['read_pages']} / {stats['total_pages']}"

        self._read_pages_var.set(text)

    def _handle_show_chart(self):
        """Näyttää pylväskaavion luetuista ja lukemattomista sivuista."""
        total_pages = 0
        read_pages = 0

        for book in self._books:
            if not isinstance(book, dict):
                continue

            pages = book.get("pages", 0)
            total_pages += pages

            if book.get("read", False):
                read_pages += pages

        unread_pages = max(total_pages - read_pages, 0)

        labels = [f"Read pages ({read_pages})",
                  f"Unread pages ({unread_pages})"]
        values = [read_pages, unread_pages]

        plt.figure()
        plt.bar(labels, values)
        plt.title("Reading progress (pages)")
        plt.ylabel("Pages")
        plt.tight_layout()
        plt.show()
