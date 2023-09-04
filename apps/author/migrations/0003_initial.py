# Generated by Django 4.2.4 on 2023-09-04 04:54

import ckeditor.fields
from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0002_delete_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('author_id', django_extensions.db.fields.RandomCharField(blank=True, editable=False, include_alpha=False, length=15, unique=True, verbose_name='Id')),
                ('author_name', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Name')),
                ('author_surname', models.CharField(max_length=50, verbose_name='Surname')),
                ('author_fullname', models.CharField(blank=True, max_length=50, null=True, verbose_name='Full Name')),
                ('author_email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email')),
                ('author_slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='author_fullname', unique=True, verbose_name='Slug')),
                ('author_description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='description')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='birthdate')),
                ('died_date', models.DateField(blank=True, null=True, verbose_name='died_date')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
    ]
