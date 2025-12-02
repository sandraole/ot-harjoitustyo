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
            "pages": pages
        }
        self._books.append(book)
        self._save_books()

    def get_all(self):
        return list(self._books)
