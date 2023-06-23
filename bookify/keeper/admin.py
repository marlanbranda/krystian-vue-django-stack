from django.contrib import admin
from .models import Book, BookISBN, Character, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'description'] # this is lets you to limit the admin to certain fields in model 
    list_display = ['title', 'description', 'price']
    list_filter = ['owned']
    search_fields = ['description']


@admin.register(BookISBN)
class BookISBNAdmin(admin.ModelAdmin):
    list_display = ['isbn_10', 'isbn_13']
    
    
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'book']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass