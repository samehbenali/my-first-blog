from django.db import models

# Create your models here.
class Nachid(models.Model):
    title_nachid = models.CharField(max_length=256, unique=True)
    nachid = models.TextField(unique=True)
    def __str__(self):
        return self.title_nachid
