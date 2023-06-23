from rest_framework import serializers
from .models import Book, BookISBN, Character, Author


class BookISBNSerialized(serializers.ModelSerializer):
    class Meta:
        model = BookISBN
        fields = ['isbn_10', 'isbn_13']


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'book']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'book']


class BookSerializer(serializers.ModelSerializer):
    isbn = BookISBNSerialized(many=False)
    characters = CharacterSerializer(many=True)
    author = AuthorSerializer(many=True)
    
    class Meta:
        model = Book
        fields = [
            'id', 
            'title', 
            'description', 
            'price', 
            'owned', 
            'isbn', 
            'characters',
            'author',
            ]


class BookMiniSerializer(serializers.ModelSerializer):
    isbn = BookISBNSerialized(many=False)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn']
