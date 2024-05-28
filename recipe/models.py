from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    day = models.CharField(max_length=50)
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.name
