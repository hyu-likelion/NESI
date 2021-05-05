from django.db import models

# Create your models here.
from django.forms import forms


class Todo(models.Model):
    content = models.TextField(max_length=100)


