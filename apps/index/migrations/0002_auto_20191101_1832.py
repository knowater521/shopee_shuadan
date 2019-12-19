# Generated by Django 2.2.6 on 2019-11-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brush_price',
            field=models.FloatField(verbose_name='刷单价格'),
        ),
        migrations.AlterField(
            model_name='product',
            name='number',
            field=models.IntegerField(verbose_name='刷单数量'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.FloatField(verbose_name='产品价格'),
        ),
    ]