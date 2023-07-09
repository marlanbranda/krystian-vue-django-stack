from django.contrib import admin
from .models import BookToRate, Rating


admin.site.register(BookToRate)
admin.site.register(Rating)