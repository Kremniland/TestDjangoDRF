# Generated by Django 4.1.5 on 2023-01-04 19:40

from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=64)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Наименование')),
                ('full_price', models.FloatField(verbose_name='Цена')),
                ('description', models.CharField(max_length=512, verbose_name='Описание')),
                ('amount', models.IntegerField(verbose_name='Колличество')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления')),
                ('exists', models.BooleanField(verbose_name='Есть ли в продаже')),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='images/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='shop.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Производитель')),
                ('slug', models.SlugField(max_length=100)),
                ('products', models.ManyToManyField(related_name='manufacturer', to='shop.product')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
    ]
