# Generated by Django 4.2.1 on 2023-05-27 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор товара'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото товара'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(default=False, verbose_name='Наличие функции LTE'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Наименование товара'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.IntegerField(verbose_name='Цена товара'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateField(verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=150, unique=True, verbose_name='URL товара'),
        ),
    ]