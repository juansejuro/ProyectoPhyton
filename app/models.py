from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad=models.IntegerField()
    correo = models.EmailField(max_length=100)
    numDoc = models.CharField(max_length=10)
    usuarioCreacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.nombre + ' ' + self.apellidos
    
    class Meta:
        db_table = 'App_Alumno'
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['nombre']
    