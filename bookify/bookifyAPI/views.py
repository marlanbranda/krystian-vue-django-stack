from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.decorators import action

from django.contrib.auth.models import User

from .models import BookToRate, Rating
from .serializers import BookTRSerializer, RatingSerializer, WideBookTRSerializer, UserSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication, )


class BookTRviewset(viewsets.ModelViewSet):
    queryset = BookToRate.objects.all()
    serializer_class =  WideBookTRSerializer
    authentication_classes = (TokenAuthentication, )

    @action(detail=True, methods=['POST'])
    def RateBook(self, request, pk=None):
        if 'stars' in request.data:
            book = BookToRate.objects.get(id=pk)
            user = request.user 
            stars = request.data['stars']
            
            try:
                rating = Rating.objects.get(user=user.id, book=book)
                rating.stars = stars
                rating.save()
                
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'rating is updated', 'result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            
            except:
                rating = Rating.objects.create(user=user, book=book, stars=stars)
                
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'rating is created', 'result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            
        else:
            response = {'message': 'you should provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class RatingViewset(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class =  RatingSerializer
    authentication_classes = (TokenAuthentication, )

    def create(self, request, *args, **kwargs):
        response = {'message': 'you can not update rating from here'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        response = {'message': 'you can not create rating from here'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
