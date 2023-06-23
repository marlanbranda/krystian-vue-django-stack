from rest_framework import serializers
from .models import Book, BookISBN, Character


class BookISBNSerialized(serializers.ModelSerializer):
    class Meta:
        model = BookISBN
        fields = ['isbn_10', 'isbn_13']


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'book']


class BookSerializer(serializers.ModelSerializer):
    isbn = BookISBNSerialized(many=False)
    characters = CharacterSerializer(many=True)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'owned', 'isbn', 'characters']
