from django.test import TestCase
from .forms import BookForm

class TestBookForm(TestCase):

    def test_book_name_is_required(self):
        form = BookForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')


    def test_edition_field_is_not_required(self):
        form = BookForm({
            'name': 'The Prophet', 
            'isbn': '039440428-9',
            'author': 'Kahlil Gibran',
            'publish_year': "1923",
            'genre': "Philosophy",
            'origin': 'Lebanese'
            })
        print(form.errors)
        self.assertTrue(form.is_valid())


    def test_fields_are_explicit_in_form_metaclass(self):
        form = BookForm()
        self.assertEqual(form.Meta.fields, ['isbn', 'name', 'author', 'publish_year', 'edition', 'genre', 'origin'])


