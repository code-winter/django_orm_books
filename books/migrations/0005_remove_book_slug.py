# Generated by Django 4.0.2 on 2022-02-15 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='slug',
        ),
    ]
