from rest_framework import serializers
from .models import Book, BookISBN


class BookISBNSerialized(serializers.ModelSerializer):
    class Meta:
        model = BookISBN
        fields = ['isbn_10', 'isbn_13']


class BookSerializer(serializers.ModelSerializer):
    isbn = BookISBNSerialized(many=False)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'owned', 'isbn']
