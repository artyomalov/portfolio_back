# Generated by Django 4.2.2 on 2023-07-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0004_rename_related_progect_imagemodel_related_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='alt_description',
            field=models.CharField(default='project image', max_length=200),
        ),
        migrations.AddField(
            model_name='previewmodel',
            name='alt_description',
            field=models.CharField(default='project preview', max_length=200),
        ),
    ]