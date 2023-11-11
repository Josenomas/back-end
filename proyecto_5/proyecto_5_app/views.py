from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    form = forms.registrousuario()
    if request.method =='POST':
        form = forms.registrousuario(request.POST)
        if form.is_valid():
            print("formulario")
            print("Nombre", form.cleaned_data['nombre'])
            print("Email", form.cleaned_data['email'])
            print("Fono", form.cleaned_data['fono'])
            
    data = {'forms': form}
    return render(request, 'index.html', data)