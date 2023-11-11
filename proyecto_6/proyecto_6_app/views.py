from django.shortcuts import render
from .models import Proyecto 

# Create your views here.

def index(request):
    return render(request,'index.html')

def listadoproyecto(request):
    proyectos = Proyecto.objects.all()
    data = {'Proyecto' : proyectos}
    return render(request,'proyectos.html',data)

