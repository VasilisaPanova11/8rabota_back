from django.contrib import admin
from .models import Material, Chart, Sell, File

# Register your models here.
admin.site.register(Material)
admin.site.register(Sell)
admin.site.register(Chart)
admin.site.register(File)
