# Generated by Django 4.2.4 on 2023-09-01 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_commodity_name_alter_market_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommodityData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Select Commodity', max_length=255, null=True, verbose_name='Commodity')),
                ('avgPrice', models.CharField(blank=True, max_length=255, null=True, verbose_name='CommodityData')),
                ('minPrice', models.CharField(blank=True, max_length=255, null=True, verbose_name='CommodityData')),
                ('maxPrice', models.CharField(blank=True, max_length=255, null=True, verbose_name='CommodityData')),
                ('priceUpdated', models.CharField(blank=True, max_length=255, null=True, verbose_name='CommodityData')),
                ('prevprice', models.CharField(blank=True, max_length=255, null=True, verbose_name='CommodityData')),
                ('commodity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.commodity')),
                ('market', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.market')),
            ],
        ),
    ]