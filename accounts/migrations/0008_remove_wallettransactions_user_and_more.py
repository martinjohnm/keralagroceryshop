# Generated by Django 4.1.2 on 2022-11-17 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_merge_20221117_0703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallettransactions',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wallettransactions',
            name='wallet',
        ),
        migrations.DeleteModel(
            name='Wallet',
        ),
        migrations.DeleteModel(
            name='WalletTransactions',
        ),
    ]
