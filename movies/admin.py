from django.contrib import admin
from .models import Movie
# Register your models here.

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(Customer)
