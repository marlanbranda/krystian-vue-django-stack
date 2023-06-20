from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    published = models.DateField(auto_now=True)
    cover = models.FileField(upload_to="covers/", default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    images = models.ImageField(upload_to="covers/", height_field=400, width_field=400,
                               default='settings.MEDIA_ROOT/logos/anonymous.jpg')
