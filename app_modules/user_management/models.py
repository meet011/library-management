from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from app_modules.core.models import BaseModel
# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseRole(models.Model):
    is_librarian = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Librarian(BaseRole):
    librarian = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='librarian_profile')

    # def __str__(self):
    #     return self.librarian.first_name or str(self.id)

class Student(BaseRole):
    student = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='student_profile')
    enroll_no = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.student.first_name or str(self.id)