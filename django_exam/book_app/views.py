from django.shortcuts import render, redirect, get_object_or_404

from .models import Book


def book_list(request):

    books = Book.objects.all().order_by('-id')

    return render(request, 'book_list.html', {
        'books': books
    })


def book_add(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Book.objects.create(
            title=title,
            author=author,
            price=price,
            description=description,
            image=image
        )

        return redirect('/books/')

    return render(request, 'book_add.html')


def book_edit(request, id):

    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':

        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.description = request.POST.get('description')

        if request.FILES.get('image'):
            book.image = request.FILES.get('image')

        book.save()

        return redirect('/books/')

    return render(request, 'book_edit.html', {
        'book': book
    })


def book_delete(request, id):

    book = get_object_or_404(Book, id=id)

    book.delete()

    return redirect('/books/')

