# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.calendar_view, name='calendar_view'),
#     path('add-event/', views.add_event, name='add_event'),
#     path('delete-event/<int:event_id>/', views.delete_event, name='delete_event'),
#     path('add-category/', views.add_category, name='add_category'),
#     path('api/events/', views.get_events_json, name='get_events_json'),
# ]




from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add-calendar/', views.calendar_view, name='calendar_view'),
    path('view-calendar/', views.calendar_view_readonly, name='calendar_view_readonly'),
    path('add-event/', views.add_event, name='add_event'),
    path('delete-event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('add-category/', views.add_category, name='add_category'),
    path('api/events/', views.get_events_json, name='get_events_json'),
]