from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn', 'name', 'author', 'publish_year', 'edition', 'genre', 'origin']