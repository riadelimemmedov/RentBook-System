# Generated by Django 4.2.4 on 2023-09-05 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customer_customer_book_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_book_count',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Book Count'),
        ),
    ]