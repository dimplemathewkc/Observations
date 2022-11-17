from django.contrib import admin
from .models import Observations, Components, ValueTypes, ValueUnits

# Register your models here.
admin.site.register(Components)
admin.site.register(ValueTypes)
admin.site.register(ValueUnits)
admin.site.register(Observations)
