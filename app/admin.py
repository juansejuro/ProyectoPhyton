from django.contrib import admin
from .models import Alumno, Cursos, Matricula

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Cursos)
admin.site.register(Matricula)


