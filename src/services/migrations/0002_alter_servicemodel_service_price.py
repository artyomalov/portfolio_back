# Generated by Django 4.2.2 on 2023-07-15 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicemodel',
            name='service_price',
            field=models.CharField(max_length=100),
        ),
    ]