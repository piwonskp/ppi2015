from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.FileField()

    def __str__(self):
        return self.title
