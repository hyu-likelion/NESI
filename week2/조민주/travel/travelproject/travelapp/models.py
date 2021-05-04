from django.db import models
# Create your models here.

class Survey(models.Model):
    survey_idx = models.AutoField(primary_key=True)
    
    questions = models.TextField(null=True)

    ans1 = models.TextField(null=True)
    ans2 = models.TextField(null=True)
    ans3 = models.TextField(null=True)
    ans4 = models.TextField(null=True)

    status = models.CharField(max_length=1, default="y")

class Result(models.Model):
    answer_idx = models.AutoField(primary_key=True)

    survey_idx = models.IntegerField()

    ans = models.TextField()


    