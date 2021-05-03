from django.db import models

class Surv(models.Model):
    surv_idx=models.AutoField(primary_key=True)
    question=models.TextField()

    ans1=models.TextField()
    ans2=models.TextField()
    ans3=models.TextField()

    valid=models.CharField(max_length=1, default='y')

class Answer(models.Model):
    ans_idx=models.AutoField(primary_key=True)

    surv_idx=models.IntegerField()

    ans=models.TextField()