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
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(12), MaxValueValidator(122)])
    gender = models.CharField(max_length=1, choices=Genders.choices)
    vaccinated = models.CharField(max_length=1, choices=Vaccinated.choices, default=Vaccinated.NO)

    class Meta:
        ordering = ['name', 'last_name', 'middle_name']
