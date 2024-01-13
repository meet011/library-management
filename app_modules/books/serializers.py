from rest_framework import serializers
from app_modules.books.models import Book, BookStatus,BorrowedBook
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'



class BookStatusSerializer(serializers.ModelSerializer):


    class Meta:
        model = BookStatus
        fields = '__all__'

class BookBorrowSerializer(serializers.ModelSerializer):

    book_status = BookStatusSerializer(many=True, required=False)

    class Meta:
        model = BorrowedBook
        fields = '__all__'
        # depth = 2


    def create(self, validated_data):
            book_status_data = validated_data.pop('book_status', [])

            borrowed_book_instance = BorrowedBook.objects.create(**validated_data)

            for status_data in book_status_data:
                BookStatus.objects.create(borrowed_book=borrowed_book_instance, **status_data)

            return borrowed_book_instance





   