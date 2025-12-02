import os
import json
import tkinter as tk
from tkinter import messagebox


class MainView(tk.Frame):
    def __init__(self, root, username, logout_handler):
        super().__init__(root, padx=10, pady=10)

        self._username = username
        self._logout_handler = logout_handler

        self._file_path = "data/books.json"
        self._books = []
        self._load_books()

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
        self._pages_entry.grid(row=2, column=1, sticky="w", padx=(5, 0))

        add_button = tk.Button(
            form_frame,
            text="Add book",
            command=self._handle_add_book
        )
        add_button.grid(row=3, column=0, columnspan=2, pady=(8, 0))

        list_frame = tk.Frame(self)
        list_frame.pack(fill="both", expand=True, pady=(10, 0))

        tk.Label(list_frame, text="Books:").pack(anchor="w")

        self._book_listbox = tk.Listbox(list_frame, width=60, height=10)
        self._book_listbox.pack(fill="both", expand=True)

        logout_button = tk.Button(
            self,
            text="Logout",
            command=self._logout_handler
        )
        logout_button.pack(pady=(10, 0), anchor="w")

        self._refresh_book_list()

    def _handle_add_book(self):
        title = self._title_entry.get().strip()
        author = self._author_entry.get().strip()
        pages = self._pages_entry.get().strip()

        if not title or not author or not pages:
            messagebox.showerror(
                "Error", "Title, author and pages are required")
            return

        try:
            pages_int = int(pages)
        except ValueError:
            messagebox.showerror("Error", "Pages must be a number")
            return

        if pages_int <= 0:
            messagebox.showerror("Error", "Pages must be positive")
            return

        self._books.append({
            "title": title,
            "author": author,
            "pages": pages_int
        })

        self._save_books()
        self._refresh_book_list()

        self._title_entry.delete(0, tk.END)
        self._author_entry.delete(0, tk.END)
        self._pages_entry.delete(0, tk.END)

    def _refresh_book_list(self):
        self._book_listbox.delete(0, tk.END)
        for book in self._books:
            if isinstance(book, dict):
                title = book.get("title", "")
                author = book.get("author", "")
                pages = book.get("pages", "")
                line = f"{title} — {author} ({pages} pages)"
            else:
                line = str(book)
            self._book_listbox.insert(tk.END, line)

    def _load_books(self):
        try:
            with open(self._file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            if isinstance(data, list):
                self._books = [
                    b for b in data
                    if isinstance(b, dict)
                    and "title" in b
                    and "author" in b
                    and "pages" in b
                ]
            else:
                self._books = []
        except FileNotFoundError:
            self._books = []
        except json.JSONDecodeError:
            self._books = []

    def _save_books(self):
        directory = os.path.dirname(self._file_path)
        if directory and not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError as e:
                print(f"Could not create directory {directory}: {e}")
        try:
            with open(self._file_path, "w", encoding="utf-8") as file:
                json.dump(self._books, file)
        except OSError as e:
            print(f"Failed to save books: {e}")
