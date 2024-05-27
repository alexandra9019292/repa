from django.shortcuts import render
from main.models import Avtor,Book

# Create your views here.
def get_page(request):
    avtors = Avtor.objects.all()
    books = Book.objects.all()
    print(books)
    for i in avtors:
        print(i, i.book_set.all())

    context = {
        'avtors':avtors,
        'books': books
    }
    return render(request, 'main.html', context)



def book_page(request):
    context = {}
    return render(request,'book.html', context)
