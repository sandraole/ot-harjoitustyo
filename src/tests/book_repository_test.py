import unittest
import os
import json
from repositories.book_repository import BookRepository


class TestBookRepository(unittest.TestCase):

    def setUp(self):
        self.test_file = "src/data/test_books.json"
        os.makedirs("src/data", exist_ok=True)

        if os.path.exists(self.test_file):
            os.remove(self.test_file)

        self.book_repository = BookRepository(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self):
        self.book_repository.add_book("Test Book", "Test Author", 123)

        books = self.book_repository.get_all()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["title"], "Test Book")
        self.assertEqual(books[0]["author"], "Test Author")
        self.assertEqual(books[0]["pages"], 123)

    def test_delete_book(self):
        self.book_repository.add_book("Book 1", "Author 1", 100)
        self.book_repository.add_book("Book 2", "Author 2", 200)
        self.book_repository.add_book("Book 3", "Author 3", 300)

        books_before = self.book_repository.get_all()
        self.assertEqual(len(books_before), 3)
        self.book_repository.delete_by_index(1)

        books_after = self.book_repository.get_all()
        self.assertEqual(len(books_after), 2)

        titles = [book["title"] for book in books_after]
        self.assertEqual(titles, ["Book 1", "Book 3"])

    def test_new_book_has_read_flag_false_by_default(self):
        self.book_repository.add_book("Test Book", "Test Author", 123)

        books = self.book_repository.get_all()
        self.assertEqual(len(books), 1)
        self.assertIn("read", books[0])
        self.assertFalse(books[0]["read"])

    def test_load_books_adds_missing(self):
        """ False """
        data = [
            {"title": "Old Book", "author": "Someone", "pages": 100}
        ]
        with open(self.test_file, "w", encoding="utf-8") as f:
            json.dump(data, f)

        repo = BookRepository(self.test_file)
        books = repo.get_all()

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["title"], "Old Book")
        self.assertIn("read", books[0])
        self.assertFalse(books[0]["read"])

    def test_set_read_status_sets_book_as_read(self):
        self.book_repository.add_book("Book 1", "Author 1", 100)
        self.book_repository.set_read_status(0, True)
        books = self.book_repository.get_all()

        self.assertTrue(books[0]["read"])

        self.book_repository.set_read_status(0, False)
        books = self.book_repository.get_all()

        self.assertFalse(books[0]["read"])

    def test_toggle_read_status_toggles(self):
        self.book_repository.add_book("Book 1", "Author 1", 100)
        books = self.book_repository.get_all()
        self.assertFalse(books[0]["read"])

        """ True """
        self.book_repository.toggle_read_status(0)
        books = self.book_repository.get_all()
        self.assertTrue(books[0]["read"])

        """ False """
        self.book_repository.toggle_read_status(0)
        books = self.book_repository.get_all()
        self.assertFalse(books[0]["read"])
