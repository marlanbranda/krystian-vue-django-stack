# Generated by Django 4.2.2 on 2023-06-21 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_alter_book_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='book',
            name='images',
        ),
    ]
