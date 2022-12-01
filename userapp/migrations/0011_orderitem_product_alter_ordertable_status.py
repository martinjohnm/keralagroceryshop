# Generated by Django 4.1.2 on 2022-11-01 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_product_instock'),
        ('userapp', '0010_alter_ordertable_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.product'),
        ),
        migrations.AlterField(
            model_name='ordertable',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Out For Delivery', 'Out For Delivery'), ('Completed', 'Completed'), ('Rejected', 'Rejected')], default='Pending', max_length=100),
        ),
    ]
