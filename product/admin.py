
# Register your models here.
from django.contrib import admin

# Register your models here.

from.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_url', 'type', 'brand', 'price', 'available','description')  
    search_fields = ('name', 'image_url', 'type', 'brand', 'price', 'available','description')  

admin.site.register(Product, ProductAdmin)