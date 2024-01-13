from django.contrib import admin
from django.urls import path
from app_modules.user_management.views import LibrarianRegistrationView, StudentRegistrationView, CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view()),
    path('librarian/register/', LibrarianRegistrationView.as_view()),
    path('student/register/', StudentRegistrationView.as_view()),
]
