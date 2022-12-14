from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Card(models.Model):
    class Vaccinated(models.TextChoices):
        YES = "Y", "Yes"
        NO = "N", "No"

    class Genders(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"

    name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=1, choices=Genders.choices)
    vaccinated = models.CharField(max_length=1, choices=Vaccinated.choices, default=Vaccinated.NO)

    class Meta:
        ordering = ['last_name', 'name', 'middle_name']
