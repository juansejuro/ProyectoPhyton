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


class Cursos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    usuarioCreacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.nombre + ' ' + self.descripcion
    
    class Meta:
        db_table = 'App_Cursos'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nombre']
        
        
class Matricula(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    nota1 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    nota2 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    nota3 = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    nota_final = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.alumno.nombre} - {self.curso.nombre}"

    class Meta:
        unique_together = ['alumno', 'curso']        