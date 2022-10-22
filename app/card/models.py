from random import choices
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Gender(models.Model):
    class Genders(models.TextChoices):
        M = "Male"
        F = "Female"
    
    gender = models.CharField(max_length=6, choices=Genders.choices, default=Genders.M)


class Vaccination(models.Model):
    class Vaccinated(models.TextChoices):
        Y = "Yes"
        N = "No"
    vaccinated = models.CharField(max_length=3, choices=Vaccinated.choices, default=Vaccinated.N)


class Card(models.Model):
    name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField(default=16, validators=[MinValueValidator(16), MaxValueValidator(122)])
    gender = models.ForeignKey("Gender", on_delete=models.PROTECT)
    vaccinated = models.ForeignKey("Vaccination", on_delete=models.PROTECT)