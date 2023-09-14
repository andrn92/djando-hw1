from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
from django.core.paginator import Paginator


def greeting(request):
    return HttpResponse('Hello everybody!')

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)

def moving_date_published(request, date_published):
    template = 'books/date_published.html'
    books = Book.objects.all()
    dates = []
    for book in books:
        dates.append(book.pub_date)
        if book.pub_date.strftime('%Y-%m-%d') == date_published:
            name = book.name
    dates.sort()
    date_start = dates[0]
    date_end = dates[-1]
    book = Book.objects.get(name=name)
    ind = dates.index(book.pub_date)
    previos_page = ''
    next_page = ''
    
    if date_start < book.pub_date < date_end:
        previos_page = dates[ind - 1].strftime('%Y-%m-%d')
        next_page = dates[ind + 1].strftime('%Y-%m-%d')
    elif book.pub_date == date_start:
        next_page = dates[ind + 1].strftime('%Y-%m-%d')
    elif book.pub_date == date_end:
        previos_page = dates[ind - 1].strftime('%Y-%m-%d')

    context = {'book': book, 'previos_page': previos_page, 'next_page': next_page}
    return render(request, template, context)
