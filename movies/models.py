from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')

    def __str__(self):
        return str(self.id) + ' - ' + self.name

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default = 1)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default = 1)
    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(1000000)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - ' + self.order_id


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - ' + self.email