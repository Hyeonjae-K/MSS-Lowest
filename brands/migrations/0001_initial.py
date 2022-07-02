# Generated by Django 4.0.5 on 2022-07-02 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ko_name', models.CharField(max_length=35)),
                ('en_name', models.CharField(max_length=50)),
                ('url', models.URLField(unique=True)),
            ],
        ),
    ]
