# Generated by Django 3.2.8 on 2022-01-10 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=140, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('pattern', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Ingredient',
                'verbose_name_plural': 'Ingredient',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=140, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('OK', 'OK'), ('SE', 'Sem estoque')], max_length=3, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ItemStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('potions', models.FloatField(default=0)),
                ('kilos', models.FloatField(default=0)),
                ('status', models.CharField(blank=True, choices=[('OK', 'OK'), ('SE', 'Sem estoque')], max_length=3, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
            ],
            options={
                'verbose_name': 'item stock',
                'verbose_name_plural': 'item stocks',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='ItemIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('potions', models.FloatField(default=0)),
                ('kilos', models.FloatField(default=0)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.ingredient')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
            ],
            options={
                'verbose_name': 'Item ingredient',
                'verbose_name_plural': 'Item ingredient',
                'ordering': ('pk',),
            },
        ),
    ]
