from django.contrib import admin
from .models import Hike
from .models import TripDetail

class TripReportInline(admin.TabularInline):
    model = TripDetail
    extra = 3

class HikeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Overview',  {'fields': ['title','place','country']}),
        ('Date Information', {'fields': ['date', 'duration']}),
        ('Image',{'fields': ['hike_image']})
    ]
    inlines = [TripReportInline]
    # this changes the layout of the dropdown list for hikes (default it shows the whole record as a str)
    list_display = ('title','place','country', 'date', 'duration','get_year')
    list_filter = ['country']

# Register your models here.
# this registers Hike to the admin site, so it will be accessable there.
admin.site.register(Hike, HikeAdmin)
admin.site.register(TripDetail)

# don't forget to add a superuser with python manage.py createsuperuser
