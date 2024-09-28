from django.contrib import admin
from .models import Service, ServiceDescription, Order, Portfolio, Tag, CategoryService


for a in [ Order, Portfolio,Tag,CategoryService]:
    admin.site.register(a)



class ServiceDescriptionInline(admin.TabularInline):
    model = ServiceDescription
    extra = 1  # How many empty forms should display for new ServiceDescription objects
    fields = ('title', 'description', 'image')  # The fields to display in the inline form

# Define the Service admin with inline ServiceDescription
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceDescriptionInline]
    list_display = ('title','category_service') 