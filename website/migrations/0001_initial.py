# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-18 02:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('store_name', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=1000)),
                ('amount_spent', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=99)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='website.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=99)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Product')),
            ],
        ),
        migrations.CreateModel(
            name='SalesRep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commission_percent', models.DecimalField(decimal_places=2, max_digits=3)),
                ('commission_total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=99)),
                ('commission_to_date', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=99)),
                ('total_sales', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=99)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='website.ProductList'),
        ),
        migrations.AddField(
            model_name='order',
            name='salesrep',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.SalesRep'),
        ),
    ]
