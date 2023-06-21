from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=500, null=False)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    creation_date = models.DateField(auto_now_add=True)
    owned = models.BooleanField(default=False)
    cover = models.FileField(upload_to="image/")

    def __str__(self) -> str:
        return self.title 