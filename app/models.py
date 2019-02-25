from datetime import datetime

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)


class Wegan(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    name = models.CharField(max_length=200)
    not_eating_from = models.DateTimeField()
    weight = models.FloatField()
    height = models.FloatField()
    sex = models.CharField(max_length=1, choices=SEX, )
    tags = models.ManyToManyField(Tag)

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
        if self.not_eating_from - datetime.now():
            return "Noob"
        if self.not_eating_from - datetime.now():
            return "herbivore"
        else:
            return "The one who does not know meat"
