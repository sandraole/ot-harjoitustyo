import json
from data.file_utils import open_for_write


class BookRepository:
    def __init__(self, file_path="data/books.json"):
        self._file_path = file_path
        self._books = []
        self._load_books()

    def _load_books(self):
        try:
            with open(self._file_path, "r", encoding="utf-8") as file:
                self._books = json.load(file)
        except FileNotFoundError:
            self._books = []
        except json.JSONDecodeError:
            self._books = []

        for book in self._books:
            if isinstance(book, dict) and "read" not in book:
                book["read"] = False

    def _save_books(self):
        try:
            with open_for_write(self._file_path) as file:
                json.dump(self._books, file)
        except OSError as e:
            print(f"Failed to save books: {e}")

    def add_book(self, title, author, pages):
        book = {
            "title": title,
            "author": author,
            "pages": pages,
            "read": False,
        }
        self._books.append(book)
        self._save_books()

    def delete_by_index(self, index: int):
        try:
            del self._books[index]
            self._save_books()
        except IndexError:
            print(f"Invalid index {index} for delete")

    def set_read_status(self, index: int, read: bool):
        try:
            book = self._books[index]
        except IndexError:
            print(f"Invalid index {index} for set_read_status")
            return

        if not isinstance(book, dict):
            print(f"Invalid book type at index {index}")
            return

        book["read"] = read
        self._save_books()

    def toggle_read_status(self, index: int):
        try:
            book = self._books[index]
        except IndexError:
            print(f"Invalid index {index} for toggle_read_status")
            return

        if not isinstance(book, dict):
            print(f"Invalid book type at index {index}")
            return

        current = book.get("read", False)
        book["read"] = not current
        self._save_books()

    def get_all(self):
        return list(self._books)
