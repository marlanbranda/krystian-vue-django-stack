from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book


class DemoView(View):

    books = Book.objects.all()

    output = ""

    for book in books:
        output += f"book title: {book.title}, book description: {book.description} <br>"

    def get(self, request):
        return HttpResponse(f'this view achieved by django View Class <br> '
                            f'{self.output}')
        #return HttpResponse(self.output)


def kyrilic(request):
    return HttpResponse('demo first view ')


def template_func(request):
    books = Book.objects.all()

    return render(request, 'first_template.html', {'books': books})
