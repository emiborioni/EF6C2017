# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Distrito(models.Model):
    """
    Se decide utilizar este modelo para la clase distrito porque es
    necesario el nombre y la cantidad de votantes,
    y en un futuro se mostrara un mapa con un marker por cada distrito
    que contenga los resultados del mismo.
    """
    nombre = models.CharField('Nombre del distrito', max_length=128)
    cantidad_votantes = models.IntegerField('Cantidad de votantes', default=0)
    latitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)
    longitude = models.DecimalField('Longitud', max_digits=14, decimal_places=10, default=0)



    def __str__(self):
        return 'Distrito {}'.format(self.nombre)

class Candidato(models.Model):
    """
    #TODO Completar segun consideraciones del desarrollador
    En este comentario escribir por que se decide modelar de esta
    forma la clase
    nombre: Le coloco nombre para poder saber a que candidato le voy a poner el voto
    ditrito: Le hago una foreign key a distrito para saber a que distrito pertence el candidato.
    """

    nombre = nombre= models.CharField(max_length= 200)
    distrito = models.ForeignKey(Distrito)
    
    def __str__(self):
        return self.nombre

    def count_voto(self):
        return Votos.objects.filter(voto=self).count()


class Votos(models.Model):
    """
    #TODO Completar segun consideraciones del desarrollador
    En este comentario escribir por que se decide modelar de esta
    forma la clase
    candidato : Hago una foreign key para decirle que los votos van a estar asignados a el candidato que yo quiero especificament
    voto : Es in Integer para que pueda escribir la cantidad de votos que saco cada candidato 
    voto nulo: Es un Integer para escribir la cantidad de votos nulos que hubo
    distrito : Hago una foreign Key para saber de que distrito son los votos 
    """
    candidato = models.ForeignKey(Candidato)
    voto = models.IntegerField(null=True)
    distrito = models.ForeignKey(Distrito)

    def __str__(self):
        return self.candidato 