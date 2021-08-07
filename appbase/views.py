from django.shortcuts import get_object_or_404, render, redirect
from .models import Book
from .forms import BookForm


# Create your views here.
def get_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, "appbase.html", context)


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_books')
        else:
            print(form.errors)
    form = BookForm()
    context = {
        'form': form
    }
    return render(request, "add_book.html", context)


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('get_books')
    form = BookForm(instance=book)
    context = {
        'form': form
    }
    return render(request, "edit_book.html", context)


def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('get_books')

