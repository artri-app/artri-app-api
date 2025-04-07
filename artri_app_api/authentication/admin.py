from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Remedy

# Configuração para o model User (customizado)
class CustomUserAdmin(UserAdmin):
    # Campos a serem exibidos na lista de usuários no Admin
    list_display = ("username", "email", "first_name", "last_name", "birth_date", "weight", "height")
    
    # Campos adicionais para edição no Admin (incluindo os campos personalizados)
    fieldsets = UserAdmin.fieldsets + (
        ("Informações Pessoais", {"fields": ("birth_date", "weight", "height")}),
    )

# Configuração para o model remedy
class RemedyAdmin(admin.ModelAdmin):
    # Campos exibidos na lista de remédios
    list_display = ("name", "user", "hour", "days_of_week", "quantity")
    
    # Filtros laterais
    list_filter = ("days_of_week", "user")
    
    # Campos de busca
    search_fields = ("name", "description")

# Registra os modelos no Admin
admin.site.register(User, CustomUserAdmin)
admin.site.register(Remedy, RemedyAdmin)