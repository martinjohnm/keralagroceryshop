# Generated by Django 4.1.2 on 2022-11-14 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0019_alter_orderitemsample_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='default_address',
            field=models.BooleanField(default=False),
        ),
    ]