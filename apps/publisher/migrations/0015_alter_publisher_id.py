# Generated by Django 4.2.4 on 2023-09-05 05:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0014_alter_publisher_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2fbddafe-4fe4-4554-b1d7-5b7ffd251335'), editable=False, primary_key=True, serialize=False, verbose_name='Id'),
        ),
    ]