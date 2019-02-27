from datetime import datetime, timedelta

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Wegan(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    name = models.CharField(max_length=200)
    not_eating_from = models.DateTimeField(auto_now=True)
    weight = models.FloatField()
    height = models.FloatField()
    sex = models.CharField(max_length=1, choices=SEX, )
    tags = models.ManyToManyField(Tag, null=True)

    def body_mass_index(self):
        return self.weight / self.height ** 2

    def physique(self):
        if self.body_mass_index() < 18.5:
            return "Underweight"
        elif self.body_mass_index() <= 25:
            return "Normal"
        else:
            return "Overweight"

    def status(self):
        if self.not_eating_from - datetime.now() < timedelta(days=100):
            return "Noob"
        elif self.not_eating_from - datetime.now() < timedelta(days=200):
            return "Herbivore"
        else:
            return "The one who does not know meat"
