from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lastname', 'phone', 'email', 'categoria', 'show')
    list_display_links = ('id', 'name', 'lastname')
    list_filter = ('categoria',)
    list_per_page = 10
    search_fields = ('nome', 'lastname')
    list_editable = ('phone', 'show')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)

