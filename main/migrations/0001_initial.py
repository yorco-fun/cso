# Generated by Django 4.2.16 on 2024-09-27 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True, unique=True, verbose_name='Заголовок')),
                ('text', models.TextField(null=True, unique=True, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Часті питання',
                'verbose_name_plural': 'Часті питання',
                'db_table': 'faq',
            },
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True, unique=True, verbose_name='Заголовок')),
                ('sub_title', models.CharField(max_length=200, null=True, unique=True, verbose_name='Підзаголовок')),
                ('text', models.TextField(null=True, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Головні статті',
                'verbose_name_plural': 'Головні статті',
                'db_table': 'main',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Посада')),
                ('responsibilities', models.TextField(null=True, verbose_name="Обов'язки")),
                ('requirements', models.TextField(null=True, verbose_name='Вимоги')),
                ('conditions', models.TextField(null=True, verbose_name='Умови роботи')),
            ],
            options={
                'verbose_name': 'Вакансію',
                'verbose_name_plural': 'Вакансії',
                'db_table': 'vacancy',
            },
        ),
    ]
