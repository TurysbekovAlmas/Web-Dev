from django.contrib import admin
from django.contrib import admin
from .models import Company, Vacancy

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')  
    search_fields = ('name', 'city')  
    list_filter = ('city',)  

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary', 'company')  
    search_fields = ('name', 'company__name')  
    list_filter = ('salary',)  
