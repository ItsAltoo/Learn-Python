from django.db import models

# Create your models here.

class Employe(models.Model):
    nama = models.CharField(null=False,max_length=100)
    umur = models.CharField(null=False,max_length=4)
    job = models.CharField(null=False,max_length=100)

    def __str__(self):
        return f"{self.nama}"
    
