from django.db import models

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
    name = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.IntegerField(10)

    def __str__(self):
        return str(self.id) + ' - ' + self.name

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(1000000)
    name = models.CharField(max_length=255)
    email = models.EmailField()


    def __str__(self):
        return str(self.id) + ' - ' + self.name


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return str(self.id) + ' - ' + self.name