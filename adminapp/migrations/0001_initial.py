# Generated by Django 4.1 on 2022-10-20 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, max_length=255000, null=True, upload_to='images/')),
                ('image2', models.ImageField(blank=True, max_length=255000, null=True, upload_to='images/')),
                ('image3', models.ImageField(blank=True, max_length=255000, null=True, upload_to='images/')),
                ('price', models.IntegerField()),
                ('total_quantity', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='adminapp.category')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
    ]