from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Remedy, TrainingReport, DailyPainReport

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

class TrainingReportAdmin(admin.ModelAdmin):
    list_display = ("user", "training", "date")
    
    list_filter = ("user", "training", "date")
    
    search_fields = ("user__username", "training__name")

class DailyPainReportAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "pain_level", "pain_location")
    
    list_filter = ("user", "date", "pain_level")
    
    search_fields = ("user__username", "pain_location")

admin.site.register(User, CustomUserAdmin)
admin.site.register(Remedy, RemedyAdmin)
admin.site.register(TrainingReport, TrainingReportAdmin)
admin.site.register(DailyPainReport, DailyPainReportAdmin)