from django.contrib import admin

# Register your models here.
from .models import Book
 
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  
    list_filter = ('publication_year',)                     
    search_fields = ('title', 'author') 
admin.site.register(Book, BookAdmin)
