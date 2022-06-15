from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # Override the inherited '__str__' method to return the Item 'name'
    def __str__(self):
        return self.name
