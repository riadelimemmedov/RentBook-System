# Generated by Django 4.2.4 on 2023-10-13 18:35

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('account', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('customer_rating', models.PositiveSmallIntegerField(default=0, verbose_name='Rating')),
                ('customer_book_count', models.PositiveSmallIntegerField(default=0, verbose_name='Book Count')),
                ('customer_books', models.ManyToManyField(blank=True, help_text='Books that are currently rented', to='book.book')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_customer', to='account.profile')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
    ]
