# Generated by Django 4.2.2 on 2023-07-22 10:09

from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField(max_length=4000)),
                ('designer_name', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='PreviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview', models.ImageField(upload_to=projects.models.upload_to_preview)),
                ('alt_description', models.CharField(default='project preview', max_length=200)),
                ('related_project', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_preview', to='projects.projectmodel')),
            ],
            options={
                'verbose_name': 'preview',
                'verbose_name_plural': 'previews',
            },
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_link', models.ImageField(upload_to=projects.models.upload_to_image)),
                ('alt_description', models.CharField(default='project projects', max_length=200)),
                ('related_project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='projects.projectmodel')),
            ],
            options={
                'verbose_name': 'projects',
                'verbose_name_plural': 'images',
            },
        ),
    ]
