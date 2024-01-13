from django.contrib import admin
from app_modules.user_management.models import Librarian, Student
# Register your models here.

admin.site.register(Librarian)
admin.site.register(Student)