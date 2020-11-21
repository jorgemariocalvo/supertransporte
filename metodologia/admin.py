from django.contrib import admin

# Register your models here.
from .models import Vigilado, GrupoVigiladoFactorSubjetivo, GrupoVigilado, VariableObjetivo, GrupoObjetivo, Indicador

admin.site.register(GrupoVigiladoFactorSubjetivo)
admin.site.register(GrupoVigilado)
admin.site.register(GrupoObjetivo)
admin.site.register(Indicador)


@admin.register(Vigilado)

class VigiladoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'departamento')
    list_filter = ('modo', 'ciudad', 'departamento', 'vigilancia')
    search_fields = ('nombre',)
    ordering = ('nombre',)
    
@admin.register(VariableObjetivo)

class VariableObjetivoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('nombre',)
    ordering = ('nombre',)