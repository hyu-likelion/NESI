from django.db import models
# Create your models here.

class Survey(models.Model):
    survey_idx = models.AutoField(primary_key=True)
    
    questions = models.TextField

    ans1 = models.TextField
    ans2 = models.TextField
    ans3 = models.TextField
    ans4 = models.TextField

class Result(models.Model):
    answer_idx = models.AutoField(primary_key=True)

    survey_idx = models.IntegerField()

    ans = models.TextField()


    