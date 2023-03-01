# Generated by Django 4.1.4 on 2023-02-28 17:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Category name')),
                ('description', models.TextField(verbose_name='category description')),
                ('status', models.CharField(choices=[('0', 'STOCK_OUT'), ('1', 'STOCK_IN')], default='0', max_length=255, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Product name')),
                ('product_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Product id')),
                ('description', models.TextField(verbose_name='Product description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[main.models.min_value_validator], verbose_name='Product price')),
                ('status', models.CharField(choices=[('0', 'InActive'), ('1', 'Active')], default='0', max_length=255, verbose_name='Product Status')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='main.category')),
            ],
            options={
                'verbose_name': 'Product',
            },
        ),
    ]
