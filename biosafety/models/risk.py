from django.db import models

class Risk(models.Model):

    code  = models.CharField('Risk code', max_length=10)
    label = models.CharField('Short description', max_length=255)
    url   = models.URLField('URL', null=True, blank=True)

    description = models.TextField('Description', null=True, blank=True)
