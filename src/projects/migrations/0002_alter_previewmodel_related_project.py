# Generated by Django 4.2.2 on 2023-10-03 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='previewmodel',
            name='related_project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='project_preview', to='projects.projectmodel'),
        ),
    ]
