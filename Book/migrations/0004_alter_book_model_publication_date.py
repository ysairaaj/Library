# Generated by Django 4.2.7 on 2023-11-27 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_book_model_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_model',
            name='publication_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
