# Generated by Django 4.1.2 on 2022-11-11 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0016_user_coupon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_coupon',
            old_name='customer',
            new_name='user',
        ),
    ]