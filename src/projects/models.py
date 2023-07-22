from django.db import models
from django.utils.translation import gettext_lazy as _


class ProjectModel(models.Model):
    title = models.CharField(
        max_length=512,
        null=False,
        blank=False)
    description = models.TextField(
        max_length=4000,
        null=False,
        blank=False)
    designer_name = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title


def upload_to_preview(instance, filename):
    return './previews/{filename}'.format(filename=filename)


class PreviewModel(models.Model):
    preview = models.ImageField(
        upload_to=upload_to_preview
    )
    alt_description = models.CharField(
        default='project preview',
        blank=False,
        null=False,
        max_length=200
    )
    related_project = models.OneToOneField(
        to=ProjectModel,
        on_delete=models.CASCADE,
        null=True, blank=False,
        related_name='project_preview'
    )

    class Meta:
        verbose_name = 'preview'
        verbose_name_plural = 'previews'

    def __str__(self):
        return f'{self.related_project.title}_{self.id}'


def upload_to_image(instance, filename):
    return './images/{filename}'.format(filename=filename)


class ImageModel(models.Model):
    image_link = models.ImageField(
        upload_to=upload_to_image
    )
    alt_description = models.CharField(
        default='project projects',
        blank=False,
        null=False,
        max_length=200
    )
    related_project = models.ForeignKey(
        to=ProjectModel,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name='images'
    )

    class Meta:
        verbose_name = 'projects'
        verbose_name_plural = 'images'

    def __str__(self):
        return f'{self.related_project.title}_{self.id}'
