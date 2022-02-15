from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils.text import slugify
from datetime import datetime

from books.models import Book


def index_view(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books_obj = Book.objects.all()
    books_list = []
    for entry in books_obj:
        if not entry.slug:
            entry.slug = entry.pub_date.strftime('%Y-%m-%d')
            entry.save()
        books_list.append(entry)
    context = {'books': books_list}

    return render(request, template, context)


def get_pages(current_date, objects):
    index = 0
    for num, book in enumerate(objects):
        if current_date == book.pub_date.strftime('%Y-%m-%d'):
            index = num
    if index == 0:
        prev_page = False
        next_page = objects[1]
        return prev_page, next_page
    elif index == len(objects) - 1:
        prev_page = objects[-2]
        next_page = False
        return prev_page, next_page
    else:
        prev_page = objects[index-1]
        next_page = objects[index+1]
        return prev_page, next_page


def book_view(request, slug):
    template = 'books/book_details.html'
    book_objects = Book.objects.order_by('pub_date')
    book_list = [book for book in book_objects]
    prev_p, next_p = get_pages(slug, book_list)
    current_book = Book.objects.get(pub_date=slug)
    context = {
        'book': current_book,
        'prev': prev_p,
        'next': next_p
        }
    return render(request, template, context)
