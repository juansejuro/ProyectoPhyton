from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    # -- Alumnos --
    #path('alumnos', login_required(views.alumnos), name='alumnos'),
    path('alumnos', views.alumnos, name='alumnos'),
    #path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('<int:id>', views.view_alumno, name='view_alumno'),
    path('agregar/', views.alumno_agregar, name='alumno_agregar'),
    path('alumnos/editar/<int:id>/', views.alumno_editar, name='alumno_editar'),
    path('alumnos/eliminar/<int:id>/', views.alumno_eliminar, name='alumno_eliminar'),
    # -- Cursos --
    path('cursos', views.cursos, name='cursos'),
    path('agregar/', views.curso_agregar, name='curso_agregar'),
    path('cursos/editar/<int:id>/', views.curso_editar, name='curso_editar'),
    path('cursos/eliminar/<int:id>/', views.curso_eliminar, name='curso_eliminar'),
    
]