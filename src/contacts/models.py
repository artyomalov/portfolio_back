from django.db import models


class ContactModel(models.Model):
    title = models.CharField(blank=False, null=False, max_length=50)
    content = models.CharField(blank=False, null=False, max_length=100)
    link = models.CharField(blank=False, null=False, max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
