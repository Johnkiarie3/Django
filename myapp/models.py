from django.db import models

from django.db import models

# Create your models here.
class Article(models.Model):
    title= models.CharField(max_length=100)


#add in the thumbnail and author later

class Client(models.Model):
    name= models.CharField(max_length=255)
    email=models.EmailField()
    age= models.IntegerField()
    quantity= models.IntegerField()
    title= models.CharField(max_length=100)
    payment= models.CharField(max_length=250)

# Create your models here.

