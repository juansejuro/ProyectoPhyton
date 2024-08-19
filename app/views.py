from django.shortcuts import render,redirect, get_object_or_404
from .models import Alumno
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

# Create your views here.
# def login(request):
#     return render(request, 'app/login.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('alumnos')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
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
        alumno=Alumno(
            nombre=request.POST["nombre"],
            apellidos=request.POST["apellidos"],
            edad=request.POST["edad"],
            correo=request.POST["correo"],
            numDoc=request.POST["numDoc"],
            usuarioCreacion=request.user,
            estado=request.POST["estado"]
            )
        # grabar producto en la BD
        alumno.save()
        return redirect('alumnos')
    else:
        return render(request, 'app/alumno_agregar.html')
    
def alumno_editar(request, id):
    #alumno = Alumno.objects.get(id=id)
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        alumno.nombre=request.POST["nombre"]
        alumno.apellidos=request.POST["apellidos"]
        alumno.edad=request.POST["edad"]
        alumno.correo=request.POST["correo"]
        alumno.numDoc=request.POST["numDoc"]
        alumno.usuarioCreacion=request.user    
        alumno.estado=request.POST["estado"]
        alumno.save()
        return redirect('alumnos')
    else:
        return render(request, 'app/alumno_editar.html', {'alumno': alumno})
    
def alumno_eliminar(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    return redirect('alumnos')

