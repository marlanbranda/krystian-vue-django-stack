# Generated by Django 4.2.2 on 2023-06-21 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keeper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.FileField(default='static/images/default_cover.png', upload_to='image/'),
        ),
    ]