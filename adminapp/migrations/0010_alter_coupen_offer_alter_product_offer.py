# Generated by Django 4.1.2 on 2022-11-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_product_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupen',
            name='offer',
            field=models.IntegerField(default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='offer',
            field=models.IntegerField(default=0, max_length=255),
        ),
    ]