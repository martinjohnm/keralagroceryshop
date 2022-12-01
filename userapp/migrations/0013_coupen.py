# Generated by Django 4.1.2 on 2022-11-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0012_cart_session_id_alter_ordertable_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupen_code', models.CharField(max_length=10)),
                ('is_expired', models.BooleanField(default=False)),
                ('discount_price', models.IntegerField(verbose_name=100)),
                ('minimum_amount', models.IntegerField(default=500)),
            ],
        ),
    ]
