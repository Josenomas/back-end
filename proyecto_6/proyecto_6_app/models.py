from django.db import models

class Proyecto(models.Model):
    # Your model fields go here

    FechaInicio = models.DateField()
    FechaTermino = models.DateField()
    Nombre = models.CharField(max_length = 50)
    Responsable = models.CharField(max_length = 50)
    Prioridad = models.IntegerField()


    