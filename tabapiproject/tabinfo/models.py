from django.db import models

# Create your models here.

class Tabinfo(models.Model):
    tab_name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=300)
    unit_mg = models.IntegerField()
    company = models.CharField(max_length=300)
    uses = models.CharField(max_length=1000)
    side_effect = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.tab_name
