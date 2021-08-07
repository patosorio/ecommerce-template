from django.test import TestCase
from .models import Book

class TestModels(TestCase):

    def test_book_string_method_returns_name(self):
        book = Book.objects.create(name="Test",isbn="03944404283", author="Kahlil ibert",publish_year="1383",genre="tst",origin="te8t")
        self.assertEqual(str(book), "Test")