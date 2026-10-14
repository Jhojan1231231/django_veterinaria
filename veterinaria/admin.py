from django.contrib import admin
from veterinaria.models import Cliente, atencion

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'email')
    search_fields = ('nombre', 'direccion', 'telefono', 'email')
    list_filter = ('nombre',)

class AtencionAdmin(admin.ModelAdmin):
    list_display = ('veterinaria', 'fecha', 'hora', 'descripcion', 'costo')
    search_fields = ('veterinaria__nombre', 'descripcion')
    list_filter = ('veterinaria', 'fecha')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(atencion, AtencionAdmin)

admin.display(description="costo")
def costo_atencion(obj):
    return f"${obj.costo:.2f}".replace(',', '.')
