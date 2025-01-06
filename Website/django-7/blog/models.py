from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    nama = models.CharField(max_length=255)
    nim = models.IntegerField(max_length=15)
    bio = models.TextField()
    
    def __str__(self):
        return f"{self.nama}"