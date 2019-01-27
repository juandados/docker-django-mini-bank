from django.db import models

class Banco(models.Model):
    name = models.CharField(max_length=40, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
