from django.db import models

# from mptt.models import MPTTModel, TreeForeignKey


class Realestate(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    img = models.CharField("URL", max_length=512)

    def __str__(self):
        return self.name
