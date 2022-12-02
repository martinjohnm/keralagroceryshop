# Generated by Django 4.1.2 on 2022-11-10 12:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminapp', '0014_remove_coupen_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupen',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='coupen',
            name='coupen_code',
            field=models.CharField(default='Default', max_length=10),
        ),
    ]