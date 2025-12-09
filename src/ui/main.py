import tkinter as tk
from tkinter import messagebox


class MainView(tk.Frame):
    def __init__(self, root, username, logout_handler, book_service):
        super().__init__(root, padx=10, pady=10)

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
            font=("Arial", 16)
        )
        title_label.pack(pady=(0, 10))

        form_frame = tk.Frame(self)
        form_frame.pack(pady=(0, 10))

        tk.Label(form_frame, text="Title").grid(row=0, column=0, sticky="w")
        self._title_entry = tk.Entry(form_frame, width=30)
        self._title_entry.grid(row=0, column=1, padx=(5, 0))

        tk.Label(form_frame, text="Author").grid(row=1, column=0, sticky="w")
        self._author_entry = tk.Entry(form_frame, width=30)
        self._author_entry.grid(row=1, column=1, padx=(5, 0))

        tk.Label(form_frame, text="Pages").grid(row=2, column=0, sticky="w")
        self._pages_entry = tk.Entry(form_frame, width=10)
        self._pages_entry.grid(row=2, column=1, padx=(5, 0), sticky="w")

        add_button = tk.Button(
            form_frame,
            text="Add book",
            command=self._handle_add_book
        )
        add_button.grid(row=3, column=0, columnspan=2,
                        pady=(10, 0), sticky="ew")

        list_frame = tk.Frame(self)
        list_frame.pack(fill="both", expand=True)

        unread_frame = tk.Frame(list_frame)
        unread_frame.pack(fill="both", expand=True, pady=(0, 5))

        unread_label = tk.Label(unread_frame, text="Unread books")
        unread_label.pack(anchor="w")

        self._unread_listbox = tk.Listbox(unread_frame, width=60, height=8)
        self._unread_listbox.pack(fill="both", expand=True)

        read_frame = tk.Frame(list_frame)
        read_frame.pack(fill="both", expand=True, pady=(5, 0))

        read_label = tk.Label(read_frame, text="Read books")
        read_label.pack(anchor="w")

        self._read_listbox = tk.Listbox(read_frame, width=60, height=8)
        self._read_listbox.pack(fill="both", expand=True)

        self._unread_listbox.bind(
            "<Double-Button-1>", self._handle_toggle_read)
        self._read_listbox.bind("<Double-Button-1>", self._handle_toggle_read)

        delete_button = tk.Button(
            list_frame,
            text="Delete selected book",
            command=self._handle_delete_book
        )
        delete_button.pack(pady=(5, 0), anchor="w")

        logout_button = tk.Button(
            self,
            text="Logout",
            command=self._logout_handler
        )
        logout_button.pack(pady=(10, 0), anchor="w")

        self._refresh_book_list()

    def _handle_add_book(self):
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
