from django.contrib import admin
from .models import Book, BookISBN

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'description'] # this is lets you to limit the admin to certain fields in model 
    list_display = ['title', 'description', 'price']
    list_filter = ['owned']
    search_fields = ['description']

@admin.register(BookISBN)
class BookISBNAdmin(admin.ModelAdmin):
    # fields = ['title', 'description'] # this is lets you to limit the admin to certain fields in model 
    list_display = ['isbn_10', 'isbn_13']
    