"""Moduuli joka vastaa kirjoihin liittyvästä sovelluslogiikasta."""

from repositories.book_repository import BookRepository


class BookService:
    """Kirjojen käsittelyn sovelluslogiikka.
    
    Varmistaa syötteiden validoinnit ja siirtää pysyväistallennuksen
    BookRepository luokalle.
    
    Attributes:
        _book_repository: Vastaa kirjojejen tallennuksesta.
    """

    def __init__(self, book_repository=None):
        """Luo uuden BookService olion.
        
        Args:
            book_repository: Siinä hetkessä käytettävä olio. Jos None,
            käytetään oletus tallennusta.
        """
        self._book_repository = book_repository or BookRepository()

    def add_book(self, title, author, pages_str):
        """Validoi ja sitten lisää uuden kirjan.
        
        Args:
            title: kirjan nimi.
            author: kirjan nimi.
            pages_str: sivumäärä.
            (kaikki ovat merkkijonoina)
            
        Raises:
            ValueError: Jos kenttä on tyhjä, sivumäärä on negatiivinen tai
            se ei ole kokonaisluku.
        """
        title = title.strip()
        author = author.strip()
        pages_str = pages_str.strip()

        if not title or not author or not pages_str:
            raise ValueError("Title, author and pages are required")

        try:
            pages = int(pages_str)
        except ValueError as exc:
            raise ValueError("Pages must be an integer") from exc

        if pages <= 0:
            raise ValueError("Pages must be positive")

        self._book_repository.add_book(title, author, pages)

    def get_books(self):
        """Palauttaa kaikki kirjat.
        
        Returns:
            Lista kirjoista.
        """
        return self._book_repository.get_all()

    def delete_book(self, index: int):
        """Poistaa kirjan valitusta indeksistä.
        
        Args:
            index: kirjan indeksi.
        """
        self._book_repository.delete_by_index(index)

    def toggle_book_read(self, index: int):
        """"Siirtää/kääntää kirjan luettu-tilaan.
        
        Args:
            index: kirjan indeksi.
        """
        self._book_repository.toggle_read_status(index)

    def get_statistics(self):
        """Laskee kirjoihin liittyvät tilastot.

        Returns:
            Sanakirja:
                total_books: kaikkien kirjojen lkm
                read_books: luettujen kirjojen lkm
                unread_books: lukemattomien kirjojen lkm
                total_pages: kaikkien kirjojen sivumäärä yht
                read_pages: luettujen kirjojen sivumäärä yht
                read_page_percentage: luettujen sivujen määrä
        """
        books = self._book_repository.get_all()

        total_books = len(books)
        read_books = 0
        total_pages = 0
        read_pages = 0

        for book in books:
            if not isinstance(book, dict):
                continue

            pages = book.get("pages", 0)
            total_pages += pages

            if book.get("read", False):
                read_books += 1
                read_pages += pages

        unread_books = total_books - read_books

        if total_pages > 0:
            read_page_percentage = (read_pages / total_pages) * 100
        else:
            read_page_percentage = 0.0

        return {
            "total_books": total_books,
            "read_books": read_books,
            "unread_books": unread_books,
            "total_pages": total_pages,
            "read_pages": read_pages,
            "read_page_percentage": read_page_percentage,
        }
