# Generated by Django 4.2.4 on 2023-09-01 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_commodity_market_state_delete_mandiprice_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='market',
            name='commodity',
        ),
        migrations.AlterField(
            model_name='commodity',
            name='name',
            field=models.CharField(default='Select Commodity', max_length=255, verbose_name='Commodity'),
        ),
        migrations.AlterField(
            model_name='market',
            name='name',
            field=models.CharField(default='Select Market', max_length=255, verbose_name='Market'),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(default='Select State', max_length=255, verbose_name='State'),
        ),
    ]
