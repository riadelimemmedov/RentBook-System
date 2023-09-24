# Generated by Django 4.2.4 on 2023-09-24 17:28

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_alter_book_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('tag_book_name', models.CharField(db_index=True, help_text='Enter book tag', max_length=50, unique=True, verbose_name='Name')),
                ('tag_book_slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='tag_book_name', unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Tag Book',
                'verbose_name_plural': 'Tags Book',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='book_tag',
            field=models.ManyToManyField(null=True, related_name='tag_book', to='book.tagbook', verbose_name='Tag Book'),
        ),
    ]