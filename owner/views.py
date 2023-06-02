from django.shortcuts import render

from owner.models import Owner


# Create your views here.
def owner_list(request):

    data_context = {
        'nombre_owner': 'Luis Pardo',
        'edad': 24,
        'pais': 'Perú'
    }
    '''p = Owner(nombre='Arturo Alonso', edad=27, dni=88884444, pais='Peru', vigente=True)
    p.save()

    p.nombre = 'Arturo Perez'
    p.save()'''
    #data_context = Owner.objects.all()
    #data_context = Owner.objects.filter(pais='Peru')
    data_context= Owner.objects.filter(pais='Peru').order_by('edad')

    return render(request, 'owner/owner_list.html', context= {'data' : data_context})