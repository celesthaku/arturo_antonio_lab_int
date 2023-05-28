from django.shortcuts import render

# Create your views here.

def catalog_list(request):

    return render(request, 'catalog/catalog_list.html')