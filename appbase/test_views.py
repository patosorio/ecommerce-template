from django.test import TestCase
from .models import Book

class TestViews(TestCase):

    def test_get_books(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appbase.html')

    
    def test_get_add_book_page(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_book.html')


    def test_get_edit_book_page(self):
        book = Book.objects.create(name="Test",isbn="12345678", author="Test Subtest", publish_year="1234",genre="test-1",origin="test-2")
        response = self.client.get(f'/edit/{book.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_book.html')
    

    def test_can_add_book(self):
        response = self.client.post('/add/', {
            'name': 'Test', 
            # ISBN num must be a real one - you can use for testing:
            'isbn': '8807813041',
            'author': 'Test Subtest',
            'publish_year': "1234",
            'genre': "test-1",
            'origin': 'test-2'})
        print(response)
        self.assertRedirects(response, '/')


    def test_can_delete_book(self):
        book = Book.objects.create(name="Test",isbn="03944404283", author="Kahlil ibert",publish_year="1383",genre="tst",origin="te8t")
        response = self.client.get(f'/delete/{book.id}')
        self.assertRedirects(response, '/')
        existing_books = Book.objects.filter(id=book.id)
        self.assertEqual(len(existing_books), 0)
    
    
    def test_can_edit_book(self):
        book = Book.objects.create(name="Test",isbn="03944404283", author="Kahlil ibert",publish_year="1383",genre="tst",origin="te8t")
        response = self.client.post(f'/edit/{book.id}', {
            'name': 'New Test', 
            # ISBN num must be a real one - you can use for testing:
            'isbn': '8807813041',
            'author': 'Test Subtest',
            'publish_year': "1234",
            'genre': "test-1",
            'origin': 'test-2'})
        updated_book = Book.objects.get(id=book.id)
        self.assertEqual(updated_book.name, 'New Test')

