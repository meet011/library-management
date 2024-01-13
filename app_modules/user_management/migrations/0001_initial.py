# Generated by Django 5.0.1 on 2024-01-11 17:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_librarian', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('librarian', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='librarian_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_librarian', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('enroll_no', models.PositiveIntegerField()),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
