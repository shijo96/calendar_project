# from django.db import models
# from django.utils import timezone

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     color = models.CharField(max_length=7, default='#3788d8')  # Hex color
    
#     class Meta:
#         verbose_name_plural = "Categories"
    
#     def __str__(self):
#         return self.name

# class Event(models.Model):
#     EVENT_TYPES = (
#         ('personal', 'Personal Event'),
#         ('personal_holiday', 'Personal Holiday'),
#         ('public_holiday', 'Public Holiday'),
#     )
    
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='personal')
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.title
    
#     class Meta:
#         ordering = ['start_date']




from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#3788d8')  # Hex color
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Event(models.Model):
    EVENT_TYPES = (
        ('personal', 'Personal Event'),
        ('personal_holiday', 'Personal Holiday'),
        ('public_holiday', 'Public Holiday'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='personal')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['start_date']