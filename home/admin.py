from django.contrib import admin
from home.models import *

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(Customer)