from django.urls import path, include
from . import views 

urlpatterns = [
    path('',views.BookList, name ='book_list'),
    path('book/<int:pk>', views.SingleBook, name = 'book_item'),
]