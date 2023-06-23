from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=500, null=False)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    creation_date = models.DateField(auto_now_add=True)
    owned = models.BooleanField(default=False)
    cover = models.FileField(upload_to="image/", default="static/images/default_cover.png")
    
    # basak = models.CharField(max_length=50, null=False)
    isbn = models.OneToOneField("BookISBN", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.title 


class BookISBN(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=14, blank=True)

    def __str__(self) -> str:
        return self.isbn_10
    

class Character(models.Model):
    name = models.CharField(max_length=60, null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='characters')

    def __str__(self) -> str:
        return self.name
    

class Author(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)
    book = models.ManyToManyField(Book, related_name='author')

    def __str__(self) -> str:
        return self.name
    