from django import forms
from proyecto_6_app.models import Proyectos

class FormProyecto (forms.ModelForm):
    class meta:
        model: Proyectos
        fields = '__all__'