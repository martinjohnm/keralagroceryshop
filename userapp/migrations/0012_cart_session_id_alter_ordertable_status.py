# Generated by Django 4.1.2 on 2022-11-05 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0011_orderitem_product_alter_ordertable_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='session_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ordertable',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Out For Delivery', 'Out For Delivery'), ('Completed', 'Completed'), ('Rejected', 'Rejected'), ('Canceled', 'Canceled')], default='Pending', max_length=100),
        ),
    ]
