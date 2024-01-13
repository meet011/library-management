from django.contrib import admin
from app_modules.books.models import Book, BookStatus, BorrowedBook

# Register your models here.

admin.site.register(Book)
admin.site.register(BorrowedBook)
admin.site.register(BookStatus)