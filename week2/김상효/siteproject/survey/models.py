from django.db import models

# Create your models here.


class Question(models.Model):
    survey_idx = models.AutoField(primary_key=True)

    title = models.TextField()

    answer1 = models.TextField()
    answer2 = models.TextField()
    answer3 = models.TextField()
    answer4 = models.TextField()

    def __str__(self):
        return self.title


class Answer(models.Model):
    answer_idx = models.AutoField(primary_key=True)

    survey_idx = models.IntegerField()

    answer = models.TextField()
