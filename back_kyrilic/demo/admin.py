from django.contrib import admin
from .models import Book


@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'description', 'price']
    list_display = ['title', 'description']
