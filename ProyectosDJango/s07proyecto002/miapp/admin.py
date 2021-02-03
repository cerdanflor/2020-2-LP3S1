from django.contrib import admin
from .models import Articulo, Categoria

# Register your models here.
class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Categoria)

