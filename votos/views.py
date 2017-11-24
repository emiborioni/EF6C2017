# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from votos.models import *


def resultado_global(request, candidato_id):
    """
    Generar la vista para devolver el resultado global de la elección.
    Tener en cuenta que tiene que tener:
    
    Cantidad total de votos por candidato: Busco en la funcion candi, dentro de voto todos los que tengan el id de ese candidato, despues en vot_candidato le pido que me pase los votos que tienen esa id

    Cantidad total de votos nulos: Busco el candidato que  se llame nulo y hago lo mismo que en la consigna anterior
    
    Porcentaje de cada candidato: con los datos de la primer consigna los multiplico *100 y lo divido por la cantidad de votos totales
    
    Porcentaje de votos nulos: con los datos de la segunda consigna los multiplico *100 y lo divido por la cantidad de votos totales
    
    Total de votos de la elección: al padron, le resto los votos de los candidatos, eso me dara las personas que no votaron, entonces esto se lo resto al total y me da la cantidad de votantes
    
    """
    context={}
    context['distritos'] = Distrito.objects.all()
    #TODO TU CODIGO AQUI
    candi = Voto.objects.get(id= candidato_id)
    cant_votos = Distrito.objects.get(cantidad_votantes)
    vot_candidato = candi.voto
    porcentaje_candi = ((vot_candidato*100)/votos_totales)
    no_votantes = (cant_votos - vot_candidato)
    total = (cant_votos - no_votantes)


    if candidato.nombre == "nulo": 
        
        nul_candi = vot_candidato
        por_nulo = ((nul_candi*100)/votos)
        return render(request,'global.html',context)

    return render(request,'global.html',context)


def resultado_distrital(request, votos):
    """
    Generar la vista para devolver el resultado distrital de la elección
    Tener en cuenta que tiene que tener:
    
    Tamaño del padrón busco en Distrito cantidad_votantes 
    
    Porcentaje de votos del distrito (respecto al padron. Ejemplo: Si el distrito tiene 1000 votantes y hay 750 votos, el porcentaje es 75%)
    
    Total de votos del distrito al padron, le resto los votos de los candidatos, eso me dara las personas que no votaron, entonces esto se lo resto al total y me da la cantidad de votantes
    
    Candidato ganador no hacer !!!!!!!!!!!!
    """
    context={}

    #TODO TU CODIGO AQUI

    padron = Distrinto.objects.get(cantidad_votantes = votos)
    votos = cantidad_votantes

    total = vot_candidato = candi.voto
    porcentaje_candi = ((vot_candidato*100)/votos_totales)

    

    distritos = Distrito.objects.all()
    return render(request,'distrital.html',context, {'todos_los_distritos':distritos})
