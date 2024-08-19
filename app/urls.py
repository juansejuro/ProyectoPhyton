from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('alumnos', views.alumnos, name='alumnos'),
    path('<int:id>', views.view_alumno, name='view_alumno'),
    path('agregar/', views.alumno_agregar, name='alumno_agregar'),
    path('editar/<int:id>/', views.alumno_editar, name='alumno_editar'),
    path('eliminar/<int:id>/', views.alumno_eliminar, name='alumno_eliminar'),
]