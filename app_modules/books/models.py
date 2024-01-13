from django.db import models
from app_modules.core.models import BaseModel
from app_modules.user_management.models import Librarian, Student

# Create your models here.

class Book(BaseModel):
    book_name = models.CharField(max_length=255, blank=True, null=True)
    isbn = models.CharField(max_length=255,unique=True,blank=True, null=True)
    description = models.TextField()
    quantity_purchased = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.book_name or str(self.id)
    
class BorrowedBook(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, blank=True, null=True, related_name='borrowed_book_student')
    book = models.ManyToManyField(Book, blank=True, null=True, related_name='borrowed_book_book')
    
    def __str__(self):
        return f"Borrowed by {self.student.student.first_name}"
    
class BookStatus(models.Model):

    AVAILABLE = "AVAILABLE"
    BORROWED = "BORROWED"

    STATUS_CHOICES = (
        (AVAILABLE, "Available"),
        (BORROWED, "Borrowed"),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    borrowed_book = models.ForeignKey(BorrowedBook, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=AVAILABLE)

    def __str__(self):
        return self.book.book_name