from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))  ,             
    path('user/',include('app_modules.user_management.urls')),
    path('books/',include('app_modules.books.urls')),
]
