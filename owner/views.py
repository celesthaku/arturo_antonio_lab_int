from django.shortcuts import render

# Create your views here.
def owner_list(request):
    data_context = {
        'nombre_owner': 'Luis Pardo',
        'edad': 24,
        'pais': 'Perú'
    }

    return render(request, 'owner/owner_list.html', data_context)