
from . import models
from django.contrib import admin, messages


@admin.register(models.Team)
class Team_Admin(admin.ModelAdmin):
    list_display = ("name" , )
    search_fields = ('name', )
    ordering = ( 'name',)
    sortable_by = ('name',)

