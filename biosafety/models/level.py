from django.db import models

class Level(models.Model):

    code  = models.CharField('Level code', max_length=10)
    label = models.CharField('Small description', max_length=255)

