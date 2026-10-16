

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

# READ operation remains the same
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# CREATE operation without forms.py
def book_create(request):
    if request.method == 'POST':
        # Grab values directly from the input tags' "name" attributes
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        # Directly save to the database using the Django ORM manager
        Book.objects.create(title=title, author=author, price=price)
        return redirect('book_list')
        
    return render(request, 'book_form.html', {'action': 'Add New'})

# UPDATE operation without forms.py
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        # Extract the updated values
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        
        # Explicitly save changes to the existing row
        book.save()
        return redirect('book_list')
        
    return render(request, 'book_form.html', {'book': book, 'action': 'Update'})

# DELETE operation remains the same
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})
