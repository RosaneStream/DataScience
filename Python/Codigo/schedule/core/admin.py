from django.contrib import admin
from core.models import Event

# Register your models here.
class Admin_Event(admin.ModelAdmin):
   list_display = ("id", "title", "initial_date", "creation_date")
   list_filter = ("user", "title", "initial_date",) #filter requires a comma at the end of the list

admin.site.register(Event, Admin_Event)
