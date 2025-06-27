from django.contrib.auth.models import AbstractUser
from django.db import models

from handmade_studio import settings


class Master(AbstractUser):
    experience_years = models.IntegerField(null=True, blank=True)
    biography = models.TextField(blank=True)

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name}), experience years: {self.experience_years}"

class JewelryType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Jewelry(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    jewelry_type = models.ForeignKey(JewelryType, on_delete=models.CASCADE)
    masters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='jewelly')

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return f"{self.title}, {self.price} {self.jewelry_type.name}"
