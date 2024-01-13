from django.shortcuts import render
from app_modules.books.serializers import BookSerializer, BookBorrowSerializer, BookStatusSerializer
from app_modules.books.models import Book, BorrowedBook, BookStatus
from rest_framework import generics
from app_modules.core.permissions import IsLibrarianPermission, IsStudentPermission

# Create your views here.
class BooksView( generics.ListAPIView,generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsStudentPermission]

class BorrowedBooksView( generics.ListAPIView,generics.CreateAPIView, generics.UpdateAPIView):
    queryset = BorrowedBook.objects.all()
    serializer_class = BookBorrowSerializer

class BookStatusView(generics.ListAPIView, generics.CreateAPIView):
    queryset = BookStatus.objects.all()
    serializer_class = BookStatusSerializer