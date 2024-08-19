from django.shortcuts import render,redirect
from .models import Alumno
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def login(request):
    return render(request, 'app/login.html')


def alumnos(request):
    if request.method == 'GET':
        print("alumno: ",Alumno.objects.all())
        return render(request, 'app/alumnos.html',{'alumnos': Alumno.objects.all()})
    else:
        return render(request, 'app/alumnos.html',{'alumnos': Alumno.objects.all()})
    

def view_alumno(request, id):
    return HttpResponseRedirect(reverse('alumnos'))


def alumno_agregar(request):
    if request.method == 'POST':
        alumno=Alumno(nombre=request.POST["nombre"],
                    apellidos=request.POST["apellidos"],
                    edad=request.POST["edad"],
                    correo=request.POST["correo"],
                    numDoc=request.POST["numDoc"],)
        # grabar producto en la BD
        alumno.save()
        return redirect('/')
    else:
        return render(request, 'app/alumnos.html',{'alumnos': Alumno.objects.all()})
    
def alumno_editar(request, id):
    if request.method == 'POST':
        alumno.nombre=request.POST["nombre"]
        alumno.apellidos=request.POST["apellidos"]
        alumno.edad=request.POST["edad"]
        alumno.correo=request.POST["correo"]
        alumno.numDoc=request.POST["numDoc"]
        alumno.save()
        return redirect('/')
    else:
        alumno = Alumno.objects.get(id=id)
        return render(request, 'app/alumno_editar.html',{'alumno': alumno})
    
def alumno_eliminar(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    return redirect('/')

