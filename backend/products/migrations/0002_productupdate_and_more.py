# Generated by Django 5.0.3 on 2024-03-13 01:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=100)),
                ('retailer', models.CharField(max_length=100)),
                ('created_time', models.DateTimeField()),
                ('price', models.FloatField(null=True)),
                ('unit', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='commonproductname',
            index=models.Index(fields=['name', 'alter_name'], name='products_co_name_1c9151_idx'),
        ),
        migrations.AddConstraint(
            model_name='product',
            constraint=models.UniqueConstraint(fields=('retailer', 'sid'), name='unique_retailer_sid'),
        ),
        migrations.AddField(
            model_name='productupdate',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]