# Generated by Django 4.2.7 on 2023-11-27 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0005_alter_book_model_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_model',
            name='uploaded_by',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
