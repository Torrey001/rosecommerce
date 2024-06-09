
# Register your models here.
from django.contrib import admin

# Register your models here.

from.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'image')  
    search_fields = ('first_name', 'last_name', 'image')  

admin.site.register(User, UserAdmin)