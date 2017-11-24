# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from votos.models import *


def resultado_global(request, candiadto_id):
    """
    Generar la vista para devolver el resultado global de la elección.
    Tener en cuenta que tiene que tener:
    Cantidad total de votos por candidato
    Cantidad total de votos nulos
    Porcentaje de cada candidato
    Porcentaje de votos nulos
    Total de votos de la elección
    """
    context={}
    context['distritos'] = Distrito.objects.all()
    #TODO TU CODIGO AQUI
    candi = Voto.objects.get(id= candidato_id)
    cant_votos = Distrito.objects.get(cantidad_votantes)
    vot_candidato = candi.voto
    porcentaje_candi = ((vot_candidato*100)/votos_totales)
    votos_totales = (cant_votos - vot_candidato)


    if candidato.nombre == "nulo": 
        
        nul_candi = vot_candidato
        por_nulo = ((nul_candi*100)/votos)
        return render(request,'global.html',context)

    return render(request,'global.html',context)


def resultado_distrital(request):
    """
    Generar la vista para devolver el resultado distrital de la elección
    Tener en cuenta que tiene que tener:
    Tamaño del padrón
    Porcentaje de votos del distrito (respecto al padron. Ejemplo: Si el distrito tiene 1000 votantes y hay 750 votos, el porcentaje es 75%)
    Total de votos del distrito
    Candidato ganador no hacer !!!!!!!!!!!!
    """
    context={}

    #TODO TU CODIGO AQUI


    distritos = Distrito.objects.all()
    return render(request,'distrital.html',context, {'todos_los_distritos':distritos})
