# Generated by Django 4.1.7 on 2023-04-07 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(default='нет автора', max_length=100),
        ),
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
