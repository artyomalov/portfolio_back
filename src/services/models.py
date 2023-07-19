from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ServiceModel(models.Model):
    service_title = models.CharField(blank=False, null=False, max_length=512)
    service_price = models.CharField(blank=False, null=False, max_length=100)
    service_info = models.TextField(blank=False, null=False, max_length=4000)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service_title

    #    validators=[MinValueValidator(0), MaxValueValidator(10000)],
    #         default=700
