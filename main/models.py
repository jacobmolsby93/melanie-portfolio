from django.db import models

# Create your models here.


class Image(models.Model):
    name = models.CharField(max_length=254)
    alt = models.CharField(max_length=254, default='')
    image = models.ImageField()
    photographer = models.CharField(max_length=254, blank=True, null=True, default='')
    model = models.CharField(max_length=254, blank=True, null=True, default='')
    designer = models.CharField(max_length=254, blank=True, null=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class PaintingImage(models.Model):
    name = models.CharField(max_length=254)
    alt = models.CharField(max_length=254, default='')
    image = models.ImageField()
    photographer = models.CharField(max_length=254, blank=True, null=True, default='')
    model = models.CharField(max_length=254, blank=True, null=True, default='')
    designer = models.CharField(max_length=254, blank=True, null=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ['-created_on']

    def __str__(self):
        return self.name