from django.shortcuts import render
from .models import Book

def index(request):
    return render(request, 'template.html')

def store(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'base.html', context)

def book_details(request, book_id):
    context={
        'book': Book.objects.get(pk=book_id),
    }
    return render(request, 'store/detail.html', context)
