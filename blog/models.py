from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=100)
    engid = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/", null=True, blank=True)

    def __str__(self):
        return self.category


class ItemMenu(models.Model):
    title = models.CharField(max_length=35, null=True, blank=True)
    image = models.ImageField(upload_to="media/", null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    active = models.BooleanField(default=True)
    eng = models.CharField(max_length=35, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    des_eng = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.title



