from repositories.book_repository import BookRepository


class BookService:
    def __init__(self, book_repository=None):
        self._book_repository = book_repository or BookRepository()

    def add_book(self, title, author, pages_str):
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
        return self._book_repository.get_all()
