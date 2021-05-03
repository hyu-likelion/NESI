from django.db import models

# Create your models here.


class Survey(models.Model):
    survey_idx = models.AutoField(primary_key=True)
    question = models.TextField(max_length=200, null=True)

    ans1 = models.TextField(null=True)
    ans2 = models.TextField(null=True)
    ans3 = models.TextField(null=True)
    ans4 = models.TextField(null=True)

    status = models.CharField(max_length=1, default="y")

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer_idx = models.AutoField(primary_key=True)
    survey_idx = models.IntegerField()
    ans = models.TextField()

    def __str__(self):
        return self.ans

