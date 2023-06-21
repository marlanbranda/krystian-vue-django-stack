from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Book


class ClassView(View):

    books = Book.objects.all()

    output = f"this many book in DB : {len(books)}"

    def get(self, request):
        return HttpResponse(f'this is by class View <br> {self.output}')
       

def function_view(request):
    return HttpResponse('foo')
