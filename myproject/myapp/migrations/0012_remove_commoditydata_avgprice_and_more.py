# Generated by Django 4.2.4 on 2023-09-06 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_commoditydata_commodity_alter_commoditydata_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commoditydata',
            name='avgPrice',
        ),
        migrations.RemoveField(
            model_name='commoditydata',
            name='commodity',
        ),
        migrations.RemoveField(
            model_name='commoditydata',
            name='maxPrice',
        ),
        migrations.RemoveField(
            model_name='commoditydata',
            name='minPrice',
        ),
        migrations.RemoveField(
            model_name='commoditydata',
            name='prevprice',
        ),
        migrations.RemoveField(
            model_name='commoditydata',
            name='priceUpdated',
        ),
    ]
