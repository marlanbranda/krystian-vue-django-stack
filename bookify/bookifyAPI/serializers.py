from rest_framework import serializers

from django.contrib.auth.models import User

from .models import BookToRate, Rating


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs ={
            'password': {
                'write_only': True, 
                'required': True
                }
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class BookTRSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookToRate
        fields = ('id', 'title', 'description')


class BookTRMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookToRate
        fields = ['title']


class RatingSerializer(serializers.ModelSerializer):
    book = BookTRMiniSerializer(many=False)
    
    class Meta:
        model = Rating
        fields = ['id', 'stars', 'user', 'book']


class MiniRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['user', 'stars']


class WideBookTRSerializer(serializers.ModelSerializer):
    ratings = MiniRatingSerializer(many=True)
    
    class Meta: 
        model = BookToRate
        fields = ['id',
                  'title', 
                  'description',
                  'ratings',
                  'quantity_ratings',
                  'average_rating',
                  ]
