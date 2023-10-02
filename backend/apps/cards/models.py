from django.db import models


# Create your models here.
class CardModel(models.Model):
    name = models.CharField(
        max_length=100,
    )
    image = models.ImageField(
        upload_to="images/",
    )  # ! don't forget install pillow

    def __str__(self):
        return self.name
