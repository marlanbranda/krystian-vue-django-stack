from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Book, Character
from django.shortcuts import render

from rest_framework import viewsets
from .serializers import BookSerializer, CharacterSerializer, BookMiniSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication, )


class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()
    authentication_classes = (TokenAuthentication, )


class BookMiniViewSet(viewsets.ModelViewSet):
    serializer_class = BookMiniSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,) 
            
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)


def template_view(request):
    
    books = Book.objects.all()

    return render(request, 'first_template.html', {'books': books})


class ClassView(View):

    books = Book.objects.all()

    output = f"this many book in DB : {len(books)}"

    def get(self, request):
        return HttpResponse(f'this is by class View <br> {self.output}')
       

def function_view(request):
    return HttpResponse('foo')
