# Generated by Django 4.0.5 on 2022-07-06 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0002_brand_suffix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='suffix',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
