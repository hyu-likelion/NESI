from django.db import models

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=200)

#class Hobby(models.Model):
    #hobby_name= models.TextField(null=True)



