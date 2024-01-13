from rest_framework import serializers
from app_modules.user_management.models import Librarian, Student
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

class LibrarianSerializer(serializers.ModelSerializer):
    librarian = UserSerializer()

    class Meta:
        model = Librarian
        fields = '__all__'

    def create(self, validated_data):
        librarian_data = validated_data.pop('librarian')
        password = librarian_data.pop('password', None)
        user_instance = User.objects.create(**librarian_data)

        if password:
            user_instance.set_password(password)
            user_instance.save()

        librarian_instance = Librarian.objects.create(librarian=user_instance, **validated_data)
        return librarian_instance
    
class StudentSerializer(serializers.ModelSerializer):
    student = UserSerializer()

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        student_data = validated_data.pop('student')
        password = student_data.pop('password', None)

        user_instance = User.objects.create(**student_data)

        if password:
            user_instance.set_password(password)
            user_instance.save()

        student_instance = Student.objects.create(student=user_instance, **validated_data)
        return student_instance

    
class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    username = serializers.CharField()

    def validate(self, data):
        username = data.get('username', '')
        email = data.get('email', '')
        password = data.get('password', '')

        user = authenticate(username=username, password=password)

        if user:
            if not user.is_active:
                raise serializers.ValidationError("User account is disabled.")
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")