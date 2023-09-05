# Generated by Django 4.2.4 on 2023-09-05 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_categorybook_book_available_copies_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_summary',
            field=models.TextField(blank=True, help_text='Summary about the book', max_length=800, null=True, verbose_name='Summary'),
        ),
    ]
