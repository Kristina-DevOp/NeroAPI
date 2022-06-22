from pydoc import describe
from django.db import models


# Datenbank Model/Gerüst für Drinks erstellen
class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

# Methode für Klasse Drink
# Gibt Name + Beschreibung wieder
    def __str__(self):
       return self.name 
       #+ ' ' + self.description

