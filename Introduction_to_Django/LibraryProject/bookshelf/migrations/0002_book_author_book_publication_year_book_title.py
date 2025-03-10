# Generated by Django 5.1.6 on 2025-02-16 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
