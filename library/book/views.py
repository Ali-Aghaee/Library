from django.shortcuts import render
from .models import Book


# Create your views here.



def BookList(request):
    queryset = Book.objects.all()
    booklist_dict = {'book_list' : queryset}
    return render(request, 'book_list.html', booklist_dict)

def SingleBook(request, pk):
    if pk:
        queryset = Book.objects.get(pk = pk)
    else:
        queryset = ''
    return render(request, 'single_book.html', {'item': queryset})
        


    
    