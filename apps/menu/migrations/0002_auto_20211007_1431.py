# Generated by Django 3.2.7 on 2021-10-07 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='max',
            field=models.IntegerField(blank=True, default=2, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='number',
            field=models.IntegerField(default=1, unique=True),
        ),
    ]