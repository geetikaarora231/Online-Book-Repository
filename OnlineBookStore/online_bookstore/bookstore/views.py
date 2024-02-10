# bookstore/views.py
from django.shortcuts import render
from .models import Book

def book_list(request):
    return render(request, 'bookstore/book_list.html')

def home(request):
    books = Book.objects.all()
    return render(request, 'bookstore/home.html', {'books': books})

def login_page(request):
    return render(request, 'bookstore/login.html')

def review_page(request):
    return render(request, 'bookstore/review.html')

def shopping_page(request):
    return render(request, 'bookstore/shopping.html')

def fiction_page(request):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    return render(request, 'bookstore/fiction.html')


def book_search(request):
    query = request.GET.get('q')  # Fetch the search query from the request

    if query:
        books = Book.objects.filter(title__icontains=query)  # Perform a case-insensitive search
    else:
        books = Book.objects.all()  # Fetch all books if no search query is provided

    return render(request, 'bookstore/search_results.html', {'books': books, 'query': query})

