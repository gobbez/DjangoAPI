from django.db import models


class PythonQuiz(models.Model):
    question = models.CharField(max_length=255)
    A = models.CharField(max_length=255)
    B = models.CharField(max_length=255)
    C = models.CharField(max_length=255)
    D = models.CharField(max_length=255)
    correct = models.CharField(max_length=255)
    points = models.IntegerField()


