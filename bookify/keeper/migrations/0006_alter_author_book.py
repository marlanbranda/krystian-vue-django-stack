# Generated by Django 4.2.2 on 2023-06-24 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keeper', '0005_alter_character_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(related_name='author', to='keeper.book'),
        ),
    ]
