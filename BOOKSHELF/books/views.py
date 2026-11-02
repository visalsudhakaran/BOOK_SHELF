from django.shortcuts import render,get_object_or_404,redirect
from .models import Book
from .forms import BookForm
# Create your views here.

#Read Book List
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html',{
        'books' : books
    })

#Read Detail
def book_detail(request, pk):
    book = get_object_or_404(Book,pk=pk)
    return render(request, 'books/book_detail.html',{
        'book' : book
    })

#CREATE BOOK
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')

    else:
        form = BookForm()
        return render(request, 'books/book_form.html', {
            'form' : form,
            'title' : 'Add Book' 
        })

#UPDATE
def book_update(request,pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm()
    return render(request, 'books/book_update_form.html', {
            'form' : form,
            'title' : 'edit_book'
        })