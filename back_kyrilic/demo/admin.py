from .models import Book
from django.contrib import admin


@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'description', 'price']
    list_display = ['title', 'description']
    list_filter = ['price']
    search_fields = ['title']