# Generated by Django 4.2.4 on 2023-09-06 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_remove_commoditydata_avgprice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commoditydata',
            name='avgPrice',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='commoditydata',
            name='maxPrice',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='commoditydata',
            name='minPrice',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='commoditydata',
            name='prevprice',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='commoditydata',
            name='priceUpdated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 6, 15, 5, 59, 663695, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='commoditydata',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='CommodityData'),
        ),
    ]
