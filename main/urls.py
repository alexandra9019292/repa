from django.contrib import admin
from django.urls import path, include

from main.views import get_page, book_page

urlpatterns = [
    path('', get_page),
    path('book/', book_page, name='book'),
]