from django.contrib import admin
from .models import Movie
# Register your models here.

from django.contrib import admin
from .models import *
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(Customer)
