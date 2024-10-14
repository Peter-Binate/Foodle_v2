from django.db import models
from recipe import values as recipes_values

# Create your models here.
class Recipe(models.Model):
    title = models.fields.CharField(max_length=30)
    category = models.fields.IntegerField(
        "Type de recette",
        choices=recipes_values.CATEGORY_NAME,
        default=0
    )
    instructions = models.fields.CharField(
        max_length=1000,
        blank=True,
        null=True
    )
    preparation_time = models.fields.DurationField(required=False)
    
