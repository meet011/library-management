# Generated by Django 5.0.1 on 2024-01-11 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('user_management', '0003_alter_librarian_librarian_alter_student_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('book_name', models.CharField(blank=True, max_length=255, null=True)),
                ('isbn', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('description', models.TextField()),
                ('quantity_purchased', models.PositiveIntegerField(default=0)),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='BorrowedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ManyToManyField(blank=True, null=True, related_name='borrowed_book_book', to='books.book')),
                ('student', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_book_student', to='user_management.student')),
            ],
        ),
        migrations.CreateModel(
            name='BookStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('AVAILABLE', 'Available'), ('BORROWED', 'Borrowed')], default='AVAILABLE', max_length=255)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('borrowed_book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.borrowedbook')),
            ],
        ),
    ]
