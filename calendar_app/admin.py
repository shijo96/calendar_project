# from django.contrib import admin
# from .models import Event, Category

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'color']

# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     list_display = ['title', 'start_date', 'end_date', 'event_type', 'category']
#     list_filter = ['event_type', 'category', 'start_date']
#     search_fields = ['title', 'description']


from django.contrib import admin
from .models import Event, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date', 'event_type', 'category']
    list_filter = ['event_type', 'category', 'start_date']
    search_fields = ['title', 'description']