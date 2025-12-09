"""Vastaa kirjojen tallennuksesta"""

import json
from data.file_utils import open_for_write


class BookRepository:
    """Kirjojen tallenuksesta ja lataamisesta vastaava luokka.
    
    Kirjat tallennetaan JSON-tiedostoon listana sanakirjoina, jonka avaimia ovat:
    title, author, pages, read
    
    Attributes: 
        _file_path: polku JSON-tiedostoon.
        _books: tämänhetkiset kirjat muistissa.
    """

    def __init__(self, file_path="data/books.json"):
        """Alustaa kirjarekisterin annetulle tiedostopolulle.
        
        Args:
            file_path: Tallenukseen käytettävän JSON-tiedoston polku.
        """
        self._file_path = file_path
        self._books = []
        self._load_books()

    def _load_books(self):
        """Lataa kirjat JSON-tiedostosta muistiin.
        
        Jos tiedosto puuttuu tai se ei ole validi, luodaan tyhjä kirjalista.
        Tiedosot, joista puuttuu "read", lisätään false
        """
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
        """Tallentaa kirjan JSON-tiedostoon."""
        try:
            with open_for_write(self._file_path) as file:
                json.dump(self._books, file)
        except OSError as e:
            print(f"Failed to save books: {e}")

    def add_book(self, title, author, pages):
        """Lisää uuden kirjan listaan ja tallentaa sen.
        
        Args:
            title: kirjan nimi.
            author: kirjailija.
            pages: sivumäärä.
        """
        book = {
            "title": title,
            "author": author,
            "pages": pages,
            "read": False,
        }
        self._books.append(book)
        self._save_books()

    def delete_by_index(self, index: int):
        """Poistaa kirjan.
        
        Jos indeksi on väärä, tulee virheilmoitus ja kirjaa ei poisteta.
        
        Args:
            index: poistettavan kirjan indeksi.
        """
        try:
            del self._books[index]
            self._save_books()
        except IndexError:
            print(f"Invalid index {index} for delete")

    def set_read_status(self, index: int, read: bool):
        """Siirtää kirjan luetuksi.
        
        Args:
            index: kirjan indeksi.
            read: True, jos kirja on luettu ja muuten False.
        """
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
        """Siirtää/kääntää kirjan luettu tilan ei luetuksi.
        
        Args:
            index: kirjan indeksi.
        """
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
        """Palauttaa kaikki kirjat listana.
        
        Returns:
            Lista sanakirjoja.
        """
        return list(self._books)
