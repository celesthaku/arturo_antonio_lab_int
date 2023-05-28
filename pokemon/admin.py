from django.contrib import admin
from pokemon.models import Datos


# Register your models here.
#admin.site.register(Datos)

@admin.register(Datos)
class DatosAdmin(admin.ModelAdmin):
    fields = ('nombre', 'numero', 'tipo')
    list_display = ('nombre', 'generacion', 'tipo')

    search_fields = ('nombre', )