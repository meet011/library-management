from django.shortcuts import render
from app_modules.user_management.serializers import LibrarianSerializer, StudentSerializer, CustomLoginSerializer
from app_modules.user_management.models import Librarian, Student

from rest_framework.authentication import SessionAuthentication


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

# Create your views here.

# class LibrarianRegistrationView(APIView):
#     def get(self, request, format=None):
#         librarians = Librarian.objects.all()
#         serializer = LibrarianSerializer(librarians, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = LibrarianSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LibrarianRegistrationView( generics.ListAPIView,generics.CreateAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer

class StudentRegistrationView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CustomLoginView(APIView):
    authentication_classes = [SessionAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = CustomLoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data
            request.session.set_expiry(0)  # Set session to expire when the browser is closed
            request.session.save()
            return Response({'user_id': user.id, 'email': user.email}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
