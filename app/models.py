from django.db import models

# Create your models here.
class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad=models.IntegerField()
    email = models.EmailField(max_length=100)
    fechaNacimiento = models.CharField(max_length=50)