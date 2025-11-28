from django.contrib import admin
from .models import CarMake, CarModel

# Inline model for CarModel to be shown inside CarMake admin
class CarModelInline(admin.TabularInline):  # or admin.StackedInline
    model = CarModel
    extra = 1  # Number of empty forms to display

# Admin class for CarModel (if you want separate management)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'make', 'car_type', 'year', 'dealer_id')
    list_filter = ('make', 'car_type', 'year')
    search_fields = ('name', 'make__name', 'dealer_id')

# Admin class for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    inlines = [CarModelInline]  # Show CarModels inline

# Register models with admin site
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
