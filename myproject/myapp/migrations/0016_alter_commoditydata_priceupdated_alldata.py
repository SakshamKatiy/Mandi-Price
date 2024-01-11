# Generated by Django 4.2.4 on 2023-09-06 19:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_market_commodity_alter_commoditydata_priceupdated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commoditydata',
            name='priceUpdated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 6, 19, 9, 23, 88964, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.CreateModel(
            name='AllData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='AllData')),
                ('avgPrice', models.CharField(blank=True, max_length=255, null=True)),
                ('minPrice', models.CharField(blank=True, max_length=255, null=True)),
                ('maxPrice', models.CharField(blank=True, max_length=255, null=True)),
                ('priceUpdated', models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 6, 19, 9, 23, 89969, tzinfo=datetime.timezone.utc), null=True)),
                ('prevprice', models.CharField(blank=True, max_length=255, null=True)),
                ('commodity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.commodity')),
            ],
        ),
    ]
