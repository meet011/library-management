from django.contrib import admin
from django.urls import path
from app_modules.books.views import BooksView,BorrowedBooksView, BookStatusView

urlpatterns = [
    path('', BooksView.as_view()),
    path("borrow/", BorrowedBooksView.as_view()),
    path("borrow/<int:pk>/", BorrowedBooksView.as_view()),
    path("status/", BookStatusView.as_view()),

]