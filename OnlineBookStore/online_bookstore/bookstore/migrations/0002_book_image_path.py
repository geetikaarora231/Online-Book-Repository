# Generated by Django 4.2.2 on 2024-01-05 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image_path',
            field=models.ImageField(default=23, upload_to='book_images/'),
            preserve_default=False,
        ),
    ]
