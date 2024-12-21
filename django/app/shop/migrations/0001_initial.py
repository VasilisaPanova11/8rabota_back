# Generated by Django 5.1.2 on 2024-11-24 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='charts/', verbose_name='График')),
            ],
            options={
                'verbose_name': 'График',
                'verbose_name_plural': 'Графики',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('file', models.FileField(upload_to='uploads/', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'PDF файл',
                'verbose_name_plural': 'PDF файлы',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('cost', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материалы',
            },
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('name', models.CharField(max_length=255, verbose_name='Имя покупателя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия покупателя')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('mat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.material', verbose_name='Материал')),
            ],
            options={
                'verbose_name': 'Продажа',
                'verbose_name_plural': 'Продажи',
            },
        ),
    ]
