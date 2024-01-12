from django.db import models

# Create your models here.
class RedirectionTable(models.Model):
    coderedirection = models.CharField(max_length=6, primary_key=True)
    urlredirection = models.URLField(max_length=2083)
    datecreation = models.DateTimeField(auto_now_add=True)
    datederniereutilisation = models.DateTimeField(null=True)
    nombreutilisation = models.PositiveIntegerField(default=0)
    