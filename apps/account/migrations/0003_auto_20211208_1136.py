# Generated by Django 3.2.8 on 2021-12-08 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20211208_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default=1, max_length=150, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]
