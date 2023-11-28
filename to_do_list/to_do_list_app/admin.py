from django.contrib import admin
from to_do_list_app.models import ToDoList

# Register your models here.




@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'date']
    list_display_links = ['id', 'date']
    list_filter = ['date']
    search_fields = ['description']
    fields = ['id', 'description', 'status', 'date']
