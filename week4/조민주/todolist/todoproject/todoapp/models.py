from django.db import models
from django.forms import forms

# Create your models here.
class Todo(models.Model):
    todolist= models.TextField(max_length=200)