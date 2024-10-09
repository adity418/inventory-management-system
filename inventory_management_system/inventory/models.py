from django.db import models

# Create your models here.

class InventoryItem(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__ (self):
        return self.name
