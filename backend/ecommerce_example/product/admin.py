from django.contrib import admin
from .models import *


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'category', 'price_bangla')
    search_fields = ['title', 'author', 'category']

admin.site.register(Book, BookAdmin)

# Register your models here.
