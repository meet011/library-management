# permissions.py
from rest_framework import permissions
from app_modules.user_management.models import Librarian, Student

class IsLibrarianPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        librarian_instance = Librarian.objects.filter(librarian=request.user).first()
        return request.user.is_authenticated and librarian_instance.is_librarian
    
class IsStudentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        student_instance = Student.objects.filter(student=request.user).first()


        return request.user.is_authenticated and student_instance.is_student
