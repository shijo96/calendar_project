    # from django.shortcuts import render, redirect, get_object_or_404
    # from django.http import JsonResponse
    # from .models import Event, Category
    # from datetime import datetime, timedelta
    # import calendar

    # def calendar_view(request):
    #     categories = Category.objects.all()
        
    #     # Get current month/year or from request
    #     year = int(request.GET.get('year', datetime.now().year))
    #     month = int(request.GET.get('month', datetime.now().month))
        
    #     # Get events for the month
    #     events = Event.objects.filter(
    #         start_date__year=year,
    #         start_date__month=month
    #     )
        
    #     context = {
    #         'categories': categories,
    #         'events': events,
    #         'current_year': year,
    #         'current_month': month,
    #         'month_name': calendar.month_name[month],
    #     }
    #     return render(request, 'calendar_app/calendar.html', context)

    # def add_event(request):
    #     if request.method == 'POST':
    #         title = request.POST.get('title')
    #         description = request.POST.get('description', '')
    #         start_date = request.POST.get('start_date')
    #         end_date = request.POST.get('end_date')
    #         event_type = request.POST.get('event_type')
    #         category_id = request.POST.get('category')
            
    #         category = None
    #         if category_id:
    #             category = Category.objects.get(id=category_id)
            
    #         Event.objects.create(
    #             title=title,
    #             description=description,
    #             start_date=start_date,
    #             end_date=end_date,
    #             event_type=event_type,
    #             category=category
    #         )
    #         return redirect('calendar_view')
        
    #     categories = Category.objects.all()
    #     return render(request, 'calendar_app/add_event.html', {'categories': categories})

    # def delete_event(request, event_id):
    #     event = get_object_or_404(Event, id=event_id)
    #     event.delete()
    #     return redirect('calendar_view')

    # def get_events_json(request):
    #     year = int(request.GET.get('year', datetime.now().year))
    #     month = int(request.GET.get('month', datetime.now().month))
        
    #     events = Event.objects.filter(
    #         start_date__year=year,
    #         start_date__month=month
    #     )
        
    #     events_list = []
    #     for event in events:
    #         color = '#dc3545'  # Red for public holidays
    #         if event.event_type == 'personal_holiday':
    #             color = '#0d6efd'  # Blue for personal holidays
    #         elif event.event_type == 'personal' and event.category:
    #             color = event.category.color
            
    #         events_list.append({
    #             'id': event.id,
    #             'title': event.title,
    #             'description': event.description,
    #             'start': event.start_date.strftime('%Y-%m-%d'),
    #             'end': event.end_date.strftime('%Y-%m-%d'),
    #             'type': event.event_type,
    #             'color': color,
    #             'category': event.category.name if event.category else None
    #         })
        
    #     return JsonResponse(events_list, safe=False)

    # def add_category(request):
    #     if request.method == 'POST':
    #         name = request.POST.get('name')
    #         color = request.POST.get('color', '#3788d8')
    #         Category.objects.create(name=name, color=color)
    #         return redirect('calendar_view')
    #     return render(request, 'calendar_app/add_category.html')





from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Event, Category
from datetime import datetime, timedelta
import calendar

def home_view(request):
    """Landing page with 2 options"""
    return render(request, 'calendar_app/home.html')

def calendar_view(request):
    """Admin calendar view - Full access to add/edit/delete"""
    categories = Category.objects.all()
    
    # Get current month/year or from request
    year = int(request.GET.get('year', datetime.now().year))
    month = int(request.GET.get('month', datetime.now().month))
    
    # Get events for the month
    events = Event.objects.filter(
        start_date__year=year,
        start_date__month=month
    )
    
    context = {
        'categories': categories,
        'events': events,
        'current_year': year,
        'current_month': month,
        'month_name': calendar.month_name[month],
    }
    return render(request, 'calendar_app/calendar.html', context)

def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        event_type = request.POST.get('event_type')
        category_id = request.POST.get('category')
        
        category = None
        if category_id:
            category = Category.objects.get(id=category_id)
        
        Event.objects.create(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            event_type=event_type,
            category=category
        )
        return redirect('calendar_view')
    
    categories = Category.objects.all()
    return render(request, 'calendar_app/add_event.html', {'categories': categories})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('calendar_view')

def get_events_json(request):
    year = int(request.GET.get('year', datetime.now().year))
    month = int(request.GET.get('month', datetime.now().month))
    
    events = Event.objects.filter(
        start_date__year=year,
        start_date__month=month
    )
    
    events_list = []
    for event in events:
        color = '#dc3545'  # Red for public holidays
        if event.event_type == 'personal_holiday':
            color = '#0d6efd'  # Blue for personal holidays
        elif event.event_type == 'personal' and event.category:
            color = event.category.color
        
        events_list.append({
            'id': event.id,
            'title': event.title,
            'description': event.description,
            'start': event.start_date.strftime('%Y-%m-%d'),
            'end': event.end_date.strftime('%Y-%m-%d'),
            'type': event.event_type,
            'color': color,
            'category': event.category.name if event.category else None
        })
    
    return JsonResponse(events_list, safe=False)

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color', '#3788d8')
        Category.objects.create(name=name, color=color)
        return redirect('calendar_view')
    return render(request, 'calendar_app/add_category.html')

def calendar_view_readonly(request):
    """Read-only calendar view - Only show events from database"""
    categories = Category.objects.all()
    
    # Get current month/year or from request
    year = int(request.GET.get('year', datetime.now().year))
    month = int(request.GET.get('month', datetime.now().month))
    
    # Get events for the month
    events = Event.objects.filter(
        start_date__year=year,
        start_date__month=month
    )
    
    context = {
        'categories': categories,
        'events': events,
        'current_year': year,
        'current_month': month,
        'month_name': calendar.month_name[month],
        'readonly': True,
    }
    return render(request, 'calendar_app/calendar_readonly.html', context)
